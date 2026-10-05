#!/usr/bin/env python3
import os
import sys


def load_env_file(path: str) -> bool:
    from dotenv import load_dotenv
    if not os.path.isfile(path):
        print("[WARN] No .env file found: using shell variables only")
        print("       Create one with: cp .env.example .env\n")
        return False
    load_dotenv(path)
    return True


def read_config() -> dict[str, str | None]:
    keys = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
            "LOG_LEVEL", "ZION_ENDPOINT"]
    return {key: os.getenv(key) for key in keys}


def get_mode(raw_mode: str | None) -> str:
    if raw_mode is None:
        return "development"
    if raw_mode not in ("development", "production"):
        print(f"[WARN] Unknown MATRIX_MODE '{raw_mode}', "
              "using development\n")
        return "development"
    return raw_mode


def mask_secret(secret: str, mode: str) -> str:
    if mode == "production" or len(secret) <= 4:
        return "********"
    return secret[:4] + "*" * (len(secret) - 4)


def describe_database(url: str) -> str:
    local_hosts = ("localhost", "127.0.0.1", "sqlite")
    if any(host in url for host in local_hosts):
        return "Local instance"
    return "Remote instance"


def find_missing(config: dict[str, str | None]) -> list[str]:
    required = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
    return [key for key in required if not config[key]]


def show_config(config: dict[str, str | None], mode: str) -> None:
    default_level = "DEBUG" if mode == "development" else "WARNING"
    database = config["DATABASE_URL"]
    api_key = config["API_KEY"]
    zion = config["ZION_ENDPOINT"]
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    if database:
        print(f"Database: {describe_database(database)}")
    else:
        print("Database: NOT CONFIGURED")
    if api_key:
        print(f"API Access: Authenticated ({mask_secret(api_key, mode)})")
    else:
        print("API Access: NOT CONFIGURED")
    print(f"Log Level: {config['LOG_LEVEL'] or default_level}")
    print(f"Zion Network: {zion if zion else 'NOT CONFIGURED'}\n")


def show_sources(config: dict[str, str | None],
                 shell_keys: set[str]) -> None:
    print("Debug - where each value came from:")
    for key, value in config.items():
        if value is None:
            source = "missing (default used)"
        elif key in shell_keys:
            source = "shell environment"
        else:
            source = ".env file"
        print(f"  {key}: {source}")
    print()


def env_is_ignored(gitignore_path: str) -> bool:
    try:
        with open(gitignore_path) as file:
            return any(line.strip() == ".env" for line in file)
    except OSError:
        return False


def security_check(base_dir: str, env_loaded: bool,
                   config: dict[str, str | None],
                   shell_keys: set[str]) -> None:
    print("Environment security check:")
    if env_is_ignored(os.path.join(base_dir, ".gitignore")):
        print("[OK] .env is listed in .gitignore")
    else:
        print("[WARN] .env is NOT in .gitignore: secrets may be committed")
    if env_loaded:
        print("[OK] .env file loaded")
    else:
        print("[INFO] Running without a .env file")
    if config["API_KEY"] == "your_api_key_here":
        print("[WARN] API_KEY still has the example value")
    overrides = [key for key in config if key in shell_keys]
    if overrides:
        print(f"[OK] Shell overrides active: {', '.join(overrides)}")
    else:
        print("[INFO] No shell overrides "
              "(try: MATRIX_MODE=production python3 oracle.py)")
    print()


def main() -> int:
    print("ORACLE STATUS: Reading the Matrix...\n")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    shell_keys = set(os.environ)
    try:
        env_loaded = load_env_file(os.path.join(base_dir, ".env"))
    except ImportError:
        print("[ERROR] python-dotenv is not installed")
        print("        Install it with: pip install -r requirements.txt")
        return 1
    config = read_config()
    mode = get_mode(config["MATRIX_MODE"])
    missing = find_missing(config)

    show_config(config, mode)
    if mode == "development":
        show_sources(config, shell_keys)
    security_check(base_dir, env_loaded, config, shell_keys)

    if missing and mode == "production":
        print(f"[ERROR] Missing required config: {', '.join(missing)}")
        print("Production refuses to start with incomplete config.")
        return 1
    if missing:
        print(f"[WARN] Missing config: {', '.join(missing)}")
        print("Development mode: continuing with partial config.\n")
    print("The Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
