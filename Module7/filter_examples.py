"""filter_examples.py
Contains several example filter functions.
"""

from vector import Vector


def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Filter out odd numbers."""
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


def filter_strings_longer_than(strings: list[str], length: int) -> list[str]:
    """Filter out strings shorter than or equal to the given length.

    Exemplifies a parameterized filter function.
    """
    result = []

    for string in strings:
        if len(string) > length:
            result.append(string)

    return result


def filter_vectors_of_magnitude_less_than(vectors: list[Vector], threshold: float) -> list[Vector]:
    """Filter out vectors with a magnitude less than the threshold.

    Exemplifies filtering objects.
    """
    result = []

    for vector in vectors:
        magnitude = (vector.x ** 2 + vector.y ** 2) ** (1 / 2)
        if magnitude < threshold:
            result.append(vector)

    return result


if __name__ == "__main__":
    print(filter_even_numbers([1, 2, 3, 4, 5]))
    # Output: [2, 4]

    print(filter_strings_longer_than(["mercury", "venus", "mars", "jupiter"], 5))
    # Output: ["mercury", "jupiter"]

    vectors = [Vector(3.0, 4.0), Vector(0.0, 6.0)]
    print(filter_vectors_of_magnitude_less_than(vectors, 6.0))
    # Output: [Vector(3.0, 4.0)]
