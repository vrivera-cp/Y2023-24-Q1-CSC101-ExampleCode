"""file_iteration_1.py
Example of iterating over lines in a file using readlines.
"""

if __name__ == '__main__':
    # Using readlines()
    with open('story.txt') as f:
        lines = f.readlines()  # reads the entire file, returning a list of strings

    # Printing each line
    for line in lines:
        print(line)
    # Note: the extra lines between each print. This is because
    # each line has a newline character at the end!

    print(r"lines[0][-1] == '\n': ", lines[0][-1] == '\n')