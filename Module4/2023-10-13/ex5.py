"""ex5.py
An example of a fruitful function with a return statement.
"""


def calculate_force(mass: float, acceleration: float) -> float:
    """Compute the required force for to apply an acceleration to a body with the given mass."""
    return mass * acceleration


if __name__ == '__main__':
    force = calculate_force(70.0, 8.0)

    print(force)
