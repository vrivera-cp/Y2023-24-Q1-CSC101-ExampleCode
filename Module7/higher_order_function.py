"""higher_order_examples.py
Contains an example of a higher-order function.
"""

from typing import Callable, List


def apply_to_each(numbers: List[int], operation: Callable[[int], int]) -> List[int]:
    """Applies a given operation to each number in the list.

    A higher-order function that takes another function as its argument.
    """
    result = []

    for number in numbers:
        transformed = operation(number)
        result.append(transformed)

    return result


# Example operations to be used with the higher-order function
def square(n: int) -> int:
    """Returns the square of n."""
    return n * n


def double(n: int) -> int:
    """Returns twice the value of n."""
    return n * 2


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    print(apply_to_each(numbers, square))
    # Output: [1, 4, 9, 16]

    print(apply_to_each(numbers, double))
    # Output: [2, 4, 6, 8]
