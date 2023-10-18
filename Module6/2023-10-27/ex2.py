"""ex1.py
An example of an __init__ method.
"""


class Cat:
    """Represents a cat."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


if __name__ == '__main__':
    mochi = Cat('Mochi', 6)

    harvest = Cat('Harvest', 6)

    print(mochi.name)
    print(mochi.age)

    print(harvest.name)
    print(harvest.age)
