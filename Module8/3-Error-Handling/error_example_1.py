"""error_example_1.py
A program that tries to read a file that doesn't exist
"""

if __name__ == '__main__':
    with open('non-existent.txt') as f:  # Will produce an error
        text = f.read()

    print(text)
