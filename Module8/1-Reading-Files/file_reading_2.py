"""file_reading_2.py
A basic file reading program using with.
"""

if __name__ == '__main__':
    # The preferred way to open files using a context manager
    with open('story.txt') as f:
        text = f.read()  # returns the entire contents of the file as a single string

    # "with" closes the file for you

    print(text)  # Output the data to the screen
