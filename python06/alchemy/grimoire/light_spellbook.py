from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if result == "INVALID":
        return f"Spell rejected: {spell_name} ({ingredients} - {result})"
    return f"Spell recorded: {spell_name} ({ingredients} - {result})"
