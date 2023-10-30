"""file_parsing_1.py
Example of converting text to numerics.
"""

if __name__ == '__main__':
    xs = []
    ys = []
    with open('data_bad.csv') as f:
        next(f)  # Skips the first line
        for line in f:
            print(f'Line {i}')

            line = line.strip()  # Remove trailing new lines

            data = line.split()  # Obtain a list of strings, separated by whitespace in the original string

            x = float(data[0])
            y = float(data[1])

            xs.append(float(data[0]))  # first column
            ys.append(float(data[1]))  # second column
    print("x values:", xs)
    print("y values:", ys)