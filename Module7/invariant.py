"""fold_with_invariant.py
Contains an example of a fold function with a loop invariant.
"""

from typing import List


def fold_product_with_invariant(numbers: List[int]) -> int:
    """Calculate the product of all numbers in the list.

    Uses a loop invariant to ensure correctness.
    """
    # Initial value of the accumulator
    accumulator = 1

    # Loop invariant: At the start of every iteration, the value of 'accumulator'
    # contains the product of all numbers from 'numbers' that we have seen so far.
    for number in numbers:
        accumulator *= number

    # At this point, 'accumulator' contains the product of all numbers in 'numbers'.
    return accumulator


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    print(fold_product_with_invariant(numbers))
    # Output: 24

    # Explanation:
    # Before the loop: accumulator = 1 (product of no numbers)
    # After 1st iteration: accumulator = 1 (product of [1])
    # After 2nd iteration: accumulator = 2 (product of [1, 2])
    # After 3rd iteration: accumulator = 6 (product of [1, 2, 3])
    # After 4th iteration: accumulator = 24 (product of [1, 2, 3, 4])
