"""fold_examples.py
Contains several example fold functions.
"""

from vector import Vector


def fold_sum(numbers: list[int]) -> int:
    """Sum up all the numbers in the list."""
    accumulator = 0

    for number in numbers:
        accumulator += number

    return accumulator


def fold_concatenate(strings: list[str], delimiter: str) -> str:
    """Concatenate all the strings in the list with the given delimiter.

    Exemplifies a parameterized fold function.
    """
    accumulator = ""

    for i, string in enumerate(strings):
        accumulator += string
        if i != len(strings) - 1:  # Don't add delimiter after last string
            accumulator += delimiter

    return accumulator


def fold_longest_vector(vectors: list[Vector]) -> Vector | None:
    """Return the vector with the largest magnitude from the list.

    Exemplifies folding objects.
    """
    if not vectors:  # Handle empty list
        return None

    accumulator = vectors[0]

    for vector in vectors:
        if (vector.x ** 2 + vector.y ** 2) > (accumulator.x ** 2 + accumulator.y ** 2):
            accumulator = vector

    return accumulator


if __name__ == "__main__":
    print(fold_sum([1, 2, 3, 4]))
    # Output: 10

    print(fold_concatenate(["apple", "banana", "cherry"], ", "))
    # Output: "apple, banana, cherry"

    vectors = [Vector(3.0, 4.0), Vector(0.0, 5.0)]
    print(fold_longest_vector(vectors))
    # Output: Vector(0.0, 5.0)
