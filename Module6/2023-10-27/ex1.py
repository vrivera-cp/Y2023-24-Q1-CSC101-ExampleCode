"""ex3.py
An example of an empty class.
"""


class Cat:
    """Represents a cat."""


if __name__ == '__main__':
    mochi = Cat()
    mochi.name = 'Mochi'
    mochi.age = 6

    harvest = Cat()
    harvest.name = 'Harvest'
    harvest.age = 5

    print(mochi.name)
    print(mochi.age)

    print(harvest.name)
    print(harvest.age)
