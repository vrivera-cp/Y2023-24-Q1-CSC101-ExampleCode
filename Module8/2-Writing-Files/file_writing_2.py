"""file_writing_2.py
A basic file writing program with new lines.
"""

if __name__ == '__main__':
    with open('hello.txt', 'w') as f:
        f.write('hello\n')
        f.write('world\n')
        # Note: these will be on separate lines
