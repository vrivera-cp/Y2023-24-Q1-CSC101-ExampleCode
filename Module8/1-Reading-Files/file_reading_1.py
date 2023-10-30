"""file_reading_1.py
A basic file reading program.
"""

if __name__ == '__main__':
    # Open files referenced by a variable
    f = open('story.txt')  # Open the file for reading by default

    text = f.read()  # returns the entire contents of the file as a single string

    f.close()  # Files should always be closed once consumed

    print(text)  # Output the data to the screen
