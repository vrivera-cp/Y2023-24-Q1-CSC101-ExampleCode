"""ex1.py
An example of a fruitful function with unexpected output.
"""


def does_it_have_it(values: list[str], desired: str) -> bool:
    """return whether the list contains the value."""
    for value in values:
        if value == desired:
            return True
        else:
            return False


if __name__ == '__main__':
    animals = ['penguin', 'otter', 'elephant', 'penguin']

    does_it_have_it(animals, 'otter')

    does_it_have_it(animals, 'penguin')

    does_it_have_it(animals, 'orangutan')
