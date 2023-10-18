"""ex4.py
An example of a void function that uses a return statement.
"""


def does_it_have_it(values: list[str], desired: str) -> None:
    """Prints whether the list contains the value."""
    for value in values:
        if value == desired:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    animals = ['penguin', 'otter', 'elephant', 'penguin']

    does_it_have_it(animals, 'otter')

    does_it_have_it(animals, 'penguin')

    does_it_have_it(animals, 'orangutan')
