"""error_example_2_fixed_1.py
A program that stops when reading a file containing bad data.
"""

if __name__ == '__main__':
    xs = []
    ys = []
    try:
        with open('data_bad.csv') as f:
            next(f)  # Skips the first line
            for line in f:
                line = line.strip()  # Remove trailing new lines

                data = line.split()  # Obtain a list of strings, separated by whitespace in the original string

                x = float(data[0])
                y = float(data[1])

                xs.append(x)  # first column
                ys.append(y)  # first column

    except ValueError:
        print("Found a bad value!")

    print("x values:", xs)
    print("y values:", ys)