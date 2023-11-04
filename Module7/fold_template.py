"""fold_template.py
Contains a generalized fold function template.
"""


def fold_template(name: list) -> str:  # Be sure to provide a descriptive parameter name and appropriate types
    """A generalized fold function that concatenates string values of each input item."""

    # Accumulator:
    # - Unlike map and filter, folds begin with a single value called the accumulator
    # - Assign it a value that, when operated upon with any value
    # from the list, it should become that same value
    # - Here, since we are concatenating strings, adding an empty
    # string anything would produce an identical string
    accumulator = ''

    for element_name in name:  # Be sure to provide descriptive names
        accumulator = accumulator + str(element_name)  # accumulator typically appears on both sides

    return accumulator


if __name__ == '__main__':
    print(fold_template([1, "Hello", True]))
    # Output: "1HelloTrue"
