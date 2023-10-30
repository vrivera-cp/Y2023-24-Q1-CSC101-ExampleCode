"""file_writing_3.py
A basic file writing program that appends text
"""

if __name__ == '__main__':
    # For appending, pass 'a' to open's second parameter
    with open('hello.txt', 'a') as f:
        # If the file doesn't exist, it will be created
        f.write('goodbye\n')