"""file_iteration_3.py
Example of stripping lines.
"""

if __name__ == '__main__':
    # Iterating on the file directly
    with open('story.txt') as f:
        for line in f:
            line = line.strip()  # returns a copy with surrounding whitespace removed
            print(line)
