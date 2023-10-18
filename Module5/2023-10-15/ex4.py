"""ex4.py
An example of a good fruitful function that always returns a value.
"""


def does_it_have_it(values: list[str], desired: str) -> bool:
    """Return whether the list contains the value."""
    for value in values:
        if value == desired:
            return True
    return False


if __name__ == '__main__':
    animals = ['penguin', 'otter', 'elephant', 'penguin']

    print(does_it_have_it(animals, 'otter'))

    print(does_it_have_it(animals, 'penguin'))

    print(does_it_have_it(animals, 'orangutan'))
