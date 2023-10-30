"""ex2.py
An example of the __str__ and __repr__ methods.

Note: as of writing, PyCharm contains a bug where the debugger shows __str__ instead of __repr__.
"""


class Cat:
    """Represents a cat."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"a {self.age}-year old cat named {self.name}"

    def __repr__(self) -> str:
        return f"Cat(name={self.name}, age={self.age})"


if __name__ == '__main__':
    mochi = Cat('Mochi', 6)
    harvest = Cat('Harvest', 5)

    print(mochi)
    print(repr(harvest))
