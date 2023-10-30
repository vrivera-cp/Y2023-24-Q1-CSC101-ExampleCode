"""ex5.py
An example of class with a list attribute.
"""
from ex2 import Cat


class CatOwner:
    """Represents a person that owns any number of cats."""

    def __init__(self, name: str, cats: list[Cat]) -> None:
        self.name = name
        self.cats = cats


if __name__ == '__main__':
    cats = [Cat('Mochi', 6), Cat('Harvest', 5)]

    professor = CatOwner('Vanessa', cats)

    print("professor.name:", professor.name)
    print("professor.cats:", professor.cats, "\n")

    print("Cats:")
    for cat in professor.cats:
        print("\t", cat.name)

    cats.pop(0)
    professor.cats.append(Cat('Pearl', 3))

    print("\nCats:")
    for cat in professor.cats:
        print("\t", cat.name)
