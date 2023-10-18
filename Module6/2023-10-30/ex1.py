"""ex3.py
An example of printing classes.
"""


class Cat:
    """Represents a cat."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


if __name__ == '__main__':
    mochi = Cat('Mochi', 6)
    harvest = Cat('Harvest', 5)

    print(mochi)
    print(harvest)
