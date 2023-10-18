"""ex3.py
An example of an erroneous fruitful function that does not always return a value.
"""


def does_it_have_it(values: list[str], desired: str) -> bool:
    """Return whether the list contains the value."""
    for value in values:
        if value == desired:
            return True


if __name__ == '__main__':
    animals = ['penguin', 'otter', 'elephant', 'penguin']

    print(does_it_have_it(animals, 'otter'))

    print(does_it_have_it(animals, 'penguin'))

    print(does_it_have_it(animals, 'orangutan'))
