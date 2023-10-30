"""ex3.py
An exercise for writing the __str__ and __repr__ methods.
"""


class Vector:
    """Represents a vector in terms of x and y position from the origin."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


if __name__ == '__main__':
    a = Vector(1.0, 0.0)
    b = Vector(0.0, 1.0)

    c = Vector(a.x + b.x, a.y + b.y)

    print('a:', a)
    print('b:', b)
    print('c:', c)
