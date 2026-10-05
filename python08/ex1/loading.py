#!/usr/bin/env python3
import importlib
import importlib.metadata
import sys


def check_dependencies() -> list[str]:
    packages: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    missing: list[str] = []
    print("Checking dependencies:")
    for name, description in packages.items():
        try:
            importlib.import_module(name)
            version = importlib.metadata.version(name)
            print(f"[OK] {name} ({version}) - {description}")
        except ImportError:
            print(f"[MISSING] {name} - not installed")
            missing.append(name)
    print()
    return missing


def show_install_instructions(missing: list[str]) -> None:
    print(f"ERROR: missing dependencies: {', '.join(missing)}\n")
    print("Install with pip:")
    print("  python3 -m venv matrix_env")
    print("  source matrix_env/bin/activate")
    print("  pip install -r requirements.txt")
    print("  python3 loading.py\n")
    print("Install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def compare_managers() -> None:
    in_venv = sys.prefix != sys.base_prefix
    print("pip vs Poetry:")
    print(f"  Current environment: {sys.prefix}")
    print(f"  Isolated: {'yes' if in_venv else 'no (global!)'}")
    print("  pip    -> reads requirements.txt, installs into the")
    print("            active environment, no lock file by default")
    print("  Poetry -> reads pyproject.toml, resolves versions,")
    print("            writes poetry.lock and manages its own venv\n")


def analyze_matrix() -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    points = 1000
    print("Analyzing Matrix data...")
    print(f"Processing {points} data points...")
    rng = np.random.default_rng()
    data = pd.DataFrame({
        "signal": rng.normal(loc=50, scale=10, size=points),
        "agents": rng.poisson(lam=3, size=points),
    })
    data["signal_trend"] = data["signal"].rolling(window=50).mean()
    print(f"Average signal: {data['signal'].mean():.2f}")
    print(f"Max agents detected: {data['agents'].max()}")

    print("Generating visualization...")
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(10, 8))
    top.plot(data["signal"], alpha=0.4, label="signal")
    top.plot(data["signal_trend"], color="red", label="trend (50 pts)")
    top.set_title("Matrix signal strength")
    top.legend()
    bottom.hist(data["agents"], bins=range(0, 12), color="green")
    bottom.set_title("Agents detected per reading")
    fig.tight_layout()
    fig.savefig("matrix_analysis.png")
    plt.close(fig)
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    missing = check_dependencies()
    if missing:
        show_install_instructions(missing)
        return
    compare_managers()
    analyze_matrix()


if __name__ == "__main__":
    main()
