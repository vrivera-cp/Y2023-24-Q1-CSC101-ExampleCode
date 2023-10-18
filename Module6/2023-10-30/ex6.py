"""ex3.py
An example of an __eq__ method.
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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y


if __name__ == '__main__':
    a = Vector(1.0, 0.0)
    b = Vector(0.0, 1.0)
    c = Vector(1.0, 0.0)

    print('a == a', a == a)
    print('a == b', a == b)
    print('a == c', a == c)
