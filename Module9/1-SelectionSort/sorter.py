"""sorter.py
Performs several selection sorts.
"""

import random

from selection_sort import selection_sort

if __name__ == '__main__':
    unordered = [3, 2, 4, 1]
    selection_sort(unordered)
    print(unordered)

    ascending = [1, 2, 3, 4]
    selection_sort(ascending)
    print(ascending)

    descending = [4, 3, 2, 1]
    selection_sort(descending)
    print(descending)

    random = [random.randint(0, 100) for i in range(5)]
    selection_sort(random)
    print(random)
