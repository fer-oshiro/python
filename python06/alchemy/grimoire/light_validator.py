def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    words = ingredients.lower().replace(",", " ").split()
    for allowed in light_spell_allowed_ingredients():
        if allowed in words:
            return "VALID"
    return "INVALID"
