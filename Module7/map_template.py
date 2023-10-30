"""map_template.py
Contains a generalized map function template.
"""


def map_template(name: list) -> list:  # Be sure to provide a descriptive parameter name and appropriate types
    """A generalized map function template to map values to themselves."""
    result = []  # Always an empty list

    for element_name in name:  # Be sure to provide descriptive names
        mapped = element_name  # assign a transformed value based on element_name
        result.append(mapped)

    return result


if __name__ == '__main__':
    print(map_template([1, 2, 3]))
    # Output: [1, 2, 3]
