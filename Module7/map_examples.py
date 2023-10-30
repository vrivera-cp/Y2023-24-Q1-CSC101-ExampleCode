"""map_examples.py
Contains several example map functions.
"""

from vector import Vector


def map_to_uppercase(strings: list[str]) -> list[str]:
    """Map each string in the list to its uppercase form."""
    result = []

    for string in strings:
        mapped = string.upper()
        result.append(mapped)

    return result


def map_to_is_greater_than(values: list[int], threshold: int) -> list[bool]:
    """Map each integer to a boolean value based on the given threshold

    Exemplifies a parameterized map function.
    """
    result = []

    for value in values:
        mapped = value > threshold
        result.append(mapped)

    return result


def map_to_magnitude(vectors: list[Vector]) -> list[float]:
    """Map each int to a boolean value based on the given threshold

    Exemplifies mapping objects.
    """
    result = []

    for vector in vectors:
        mapped = (vector.x ** 2 + vector.y ** 2) ** (1 / 2)
        result.append(mapped)

    return result


if __name__ == "__main__":
    print(map_to_uppercase(["hello", "world"]))
    # Output: ['HELLO', 'WORLD']

    print(map_to_is_greater_than([1, 2, 3, 4], 3))
    # Output: [False, False, False, True]

    vectors = [Vector(3.0, 4.0), Vector(0.0, 5.0)]
    print(map_to_magnitude(vectors))
    # Output: [5.0, 5.0]
