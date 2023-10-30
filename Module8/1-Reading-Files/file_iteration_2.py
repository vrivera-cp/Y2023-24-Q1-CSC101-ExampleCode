"""file_iteration_2.py
Example of iterating over lines in a file directly.
"""

if __name__ == '__main__':
    # Iterating on the file directly
    with open('story.txt') as f:
        for line in f:  # reads each line one-by-one
            print(line)

    # Note: the extra lines between each print. This is because
    # each line has a newline character at the end!
