"""error_example_2_fixed_3.py
A program that continues to read a file containing bad data.
"""

if __name__ == '__main__':
    xs = []
    ys = []
    with open('data_bad.csv') as f:
        next(f)  # Skips the first line
        for line in f:
            line = line.strip()  # Remove trailing new lines

            data = line.split()  # Obtain a list of strings, separated by whitespace in the original string

            try:
                x = float(data[0])
                y = float(data[1])
            except ValueError:
                continue  # If this line is problematic, ignore it and consider the next line
            except IndexError:
                continue  # If this line is problematic, ignore it and consider the next line

            xs.append(x)  # first column
            ys.append(y)  # second column

    print("x values:", xs)
    print("y values:", ys)
