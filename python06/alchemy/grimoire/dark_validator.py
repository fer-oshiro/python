from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    words = ingredients.lower().replace(",", " ").split()
    for allowed in dark_spell_allowed_ingredients():
        if allowed in words:
            return "VALID"
    return "INVALID"
