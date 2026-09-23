from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    splited_ingredients: list[str] = str.split(ingredients)
    for ingredient in splited_ingredients:
        if str.lower(ingredient) in dark_spell_allowed_ingredients():
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
