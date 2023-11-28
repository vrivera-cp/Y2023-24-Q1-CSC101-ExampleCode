"""insertion_sort.py
An in-place implementation of insertion sort.
"""
from swap import swap


def insertion_sort(x: list[int]) -> None:
    """Perform an in-place insertion sort"""

    # Outer iteration over each position in the list
    for i in range(len(x)):
        # Insert or "slide" the current value to its sorted position
        for j in range(i, 0, -1):
            # Slide the value to the left until there's nothing smaller
            if x[j] < x[j - 1]:
                swap(x, j, j - 1)
            # If there isn't anything smaller we're sorted up to i
            else:
                break  # This makes insertion sort faster than selection sort
