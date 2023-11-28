"""sorter.py
Performs several insertion sorts.
"""

import random

from insertion_sort import insertion_sort

if __name__ == '__main__':
    unordered = [3, 2, 4, 1]
    insertion_sort(unordered)
    print(unordered)

    ascending = [1, 2, 3, 4]
    insertion_sort(ascending)
    print(ascending)

    descending = [4, 3, 2, 1]
    insertion_sort(descending)
    print(descending)

    random = [random.randint(0, 100) for i in range(5)]
    insertion_sort(random)
    print(random)
