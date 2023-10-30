"""filter_template.py
Contains a generalized filter function template.
"""


def filter_template(name: list) -> list:  # Be sure to provide a descriptive parameter name and the appropriate type
    """A generalized filter function that filters out non-truthy values."""
    result = []  # Always an empty list

    for element_name in name:  # Be sure to provide descriptive names
        if element_name:  # Use a different predicate here
            result.append(element_name)

    return result


if __name__ == '__main__':
    print(filter_template([0, 1, 2]))
    # Output: [1, 2]
    # Note: Zero evaluates to False in a boolean expression, because it is not truthy!
