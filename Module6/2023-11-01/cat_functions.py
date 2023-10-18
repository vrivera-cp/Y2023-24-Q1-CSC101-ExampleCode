"""cat_functions.py
Defines function(s) related to cats.
"""

from cat_owner import Cat, CatOwner


def owns_cat(owner: CatOwner, cat: Cat) -> bool:
    for owned_cat in owner.cats:
        if cat == owned_cat:
            return True
    return False
