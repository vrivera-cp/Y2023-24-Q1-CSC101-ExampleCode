"""error_example_2_fixed_4.py
A program with a comprehensive set of try/except blocks.
"""

if __name__ == '__main__':
    xs = []
    ys = []
    try:
        with open('non-existent.csv') as f:
            next(f)  # Skips the first line
            for line in f:
                line = line.strip()  # Remove trailing new lines

                data = line.split()  # Obtain a list of strings, separated by whitespace in the original string

                try:
                    x = float(data[0])
                    y = float(data[1])
                except (ValueError, IndexError):
                    # Occurs if either a ValueError or IndexError occurs
                    continue

                xs.append(x)  # first column
                ys.append(y)  # second column

    except FileNotFoundError:
        print("File not found!")
    else:
        # Occurs after try if no exception occurred
        print("x values:", xs)
        print("y values:", ys)
    finally:
        # Occurs after everything else (even if a function returned in any block!)
        print('All done!')