"""swap.py
Defines a method to perform an in-place swap between two lists elements.
"""


def swap(x: list[int], i: int, j: int) -> None:
    temp = x[i]  # Remember the value at "i" so it is not lost
    x[i] = x[j]  # Copy the value at "j" to the "i" position, erasing the previously remembered value
    x[j] = temp  # Copy the remembered value to the "j" position
