"""ex4.py
An example of a void function with unexpected output.
"""


def does_it_have_it(values: list[str], desired: str) -> None:
    """Prints whether the list contains the value."""
    for value in values:
        if value == desired:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    animals = ['penguin', 'otter', 'elephant', 'penguin']

    print("Checking for otter")
    does_it_have_it(animals, 'otter')

    print("Checking for penguin")
    does_it_have_it(animals, 'penguin')

    print("Checking for orangutan")
    does_it_have_it(animals, 'orangutan')
