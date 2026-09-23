

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    splited_ingredients: list[str] = str.split(ingredients)
    for ingredient in splited_ingredients:
        if str.lower(ingredient) in light_spell_allowed_ingredients():
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
