"""ex1.py
An example of a void function definition.
"""

def greet(entity: str) -> None:
    """Print a greeting for the given entity."""
    print('Hello ' + entity)


if __name__ == '__main__':
    greet("CSC 101")

    greet("Mochi")
