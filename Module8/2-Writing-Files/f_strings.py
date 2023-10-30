"""f_strings.py
An example of using f-strings when writing to a file.
"""
from vector import Vector

if __name__ == '__main__':
    # Create a list of vectors
    vectors = [Vector(0.0, 1.0), Vector(3.0, 4.0), Vector(100.0, 0.0)]

    with open('vectors.txt', 'w') as f:
        # Write the number of vectors
        f.write(f'# of Vectors: {len(vectors)}\n')

        # Notes:
        # - F-strings are specified with an "f" before the first quotation mark
        # - In an f-string, expressions can be placed in curly brackets
        # - Expressions are evaluated, then converted to a string, then embedded in the original string
        # - The "f" in-front of the string is completely unrelated to our variable f

        # Write each vector's data
        for i in range(len(vectors)):
            # Obtain the element because we are iterating on indices
            vector = vectors[i]

            # Calculate the vector's magnitude
            magnitude = (vector.x ** 2 + vector.y ** 2) ** (1 / 2)

            # Write the object's __str__ and then the magnitude
            f.write(f'Vector {i + 1}: {vector}\tMagnitude: {magnitude:.2f}\n')

            # Notes:
            # - The '\t' escape character represents a tab indent
            # - The precision of a floating-point number can be given (here it's to two places after the decimal)
            # - There are other formatting options available
            # - See https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals

    # Important: we are NOT printing anything in this file.
