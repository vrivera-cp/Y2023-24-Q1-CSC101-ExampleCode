"""ex3.py
An example of functions using a class directly and indirectly.
"""
from math import sqrt, atan2, pi
from vector import Vector


def get_magnitude(x: float, y: float) -> float:
    """Returns a xy-coordinate's distance from the origin."""
    return sqrt(x * x + y * y)


def get_direction(v: Vector) -> float:
    """Return the direction of the vector in degrees."""
    return atan2(v.y, v.x) * 180 / pi


if __name__ == '__main__':
    vector = Vector(1.0, 1.0)

    magnitude = get_magnitude(vector.x, vector.y)

    direction = get_direction(vector)

    print(f'(Note: sqrt(2) = {sqrt(2)})\n')

    print(f'Magnitude: {magnitude}')

    print(f'Direction: {direction}°')
