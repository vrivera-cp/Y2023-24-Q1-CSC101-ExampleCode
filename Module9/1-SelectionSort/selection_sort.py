"""selection_sort.py
An in-place implementation of selection sort.
"""
from swap import swap


def selection_sort(x: list[int]) -> None:
    """Perform an in-place selection sort"""

    # Outer iteration over each position in the list
    for i in range(len(x)):
        # Search through the remaining values for the smallest value
        next_smallest_value = x[i]
        next_smallest_value_index = i
        for j in range(i + 1, len(x)):
            # Record any smaller value and its position
            if x[j] < next_smallest_value:
                next_smallest_value = x[j]
                next_smallest_value_index = j

        # Swap the next smallest value to the current position
        swap(x, i, next_smallest_value_index)
