"""ex3.py
An example of comparing classes using the equality operator.
"""


class Vector:
    """Represents a vector in terms of x and y position from the origin."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"


if __name__ == '__main__':
    a = Vector(1.0, 0.0)
    b = Vector(0.0, 1.0)
    c = Vector(1.0, 0.0)

    print('a == a', a == a)
    print('a == b', a == b)
    print('a == c', a == c)
