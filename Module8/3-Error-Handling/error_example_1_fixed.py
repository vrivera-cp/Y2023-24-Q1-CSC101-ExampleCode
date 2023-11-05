"""error_example_1_fixed.py
A program that tries to read a file that doesn't exist and catches any errors.
"""

if __name__ == '__main__':
    try:
        # Python "tries" to execute the code within this block
        with open('non-existent.txt') as f:  # Will produce an error
            text = f.read()
        print(text)
    except FileNotFoundError:
        # This block is executed if a FileNotFoundError occurs within the "try" block
        print("Couldn't find the file!")

    # Result: We handled the error and don't see it in the console!
