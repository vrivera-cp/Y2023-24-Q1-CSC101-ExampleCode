"""functions.py
Defines several functions for usage in examples
"""


def calculate_force(mass: float, acceleration: float) -> float:
    """Compute the required force for to apply an acceleration to a body with the given mass."""
    return mass * acceleration


def add_all(numbers: list[int]) -> int:
    """Return the value of all numbers in the list added together."""
    total = 0
    for number in numbers:
        total += number
    return total


def repeat(value: int | str | bool, count: int) -> list[int] | list[str] | list[bool]:
    """Return a list containing a repeated single value."""
    repeated = []
    while len(repeated) < count:
        repeated.append(value)
    return repeated
