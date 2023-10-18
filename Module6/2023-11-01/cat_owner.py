"""cat_owner.py
Defines the Cat and CatOwner classes with __str__, __repr__, and __eq__ methods.
"""


class Cat:
    """Represents a cat."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Cat(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        return f"Cat(name={self.name}, age={self.age})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cat):
            return False
        return self.name == other.name and self.age == other.age


class CatOwner:
    """Represents a person that owns any number of cats."""

    def __init__(self, name: str, cats: list[Cat]) -> None:
        self.name = name
        self.cats = cats

    def __str__(self) -> str:
        return f"CatOwner(x={self.name}, y={self.cats})"

    def __repr__(self) -> str:
        return f"CatOwner(x={self.name}, y={self.cats})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CatOwner):
            return False
        return self.name == other.name and self.cats == other.cats
