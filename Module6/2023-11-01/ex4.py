"""ex4.py
An example of a non-pure function that aliases an object.
"""
from vector import Vector
from ex3 import get_magnitude


def scale(v: Vector, a: float) -> None:
    """Scales the vector's coordinates by the given amount"""
    v.x *= a
    v.y *= a


if __name__ == '__main__':
    vector = Vector(3.0, 4.0)

    magnitude_before = get_magnitude(vector.x, vector.y)
    print(f'Magnitude: {magnitude_before}')

    scale(vector, 4.0)

    magnitude_after = get_magnitude(vector.x, vector.y)
    print(f'Magnitude: {magnitude_after}')
