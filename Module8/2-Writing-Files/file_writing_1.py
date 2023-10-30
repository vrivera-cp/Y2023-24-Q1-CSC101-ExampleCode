"""file_writing_1.py
A basic file writing program.
"""

if __name__ == '__main__':
    # For writing, pass 'w' to open's second parameter
    with open('hello.txt', 'w') as f:
        # Once open runs, it creates an empty file called "hello.txt"
        # Important: If "hello.txt" already existed, the original is deleted forever

        f.write('hello')  # Writes a string to the file
        f.write('world')
        # Note: these will be on the same line in the output file!
