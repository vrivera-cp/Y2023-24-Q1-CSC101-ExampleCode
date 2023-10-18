"""ex2.py
An example of building a string.
"""

my_string = 'Hello'

new_string = ''
for character in my_string:
    if character == 'H':
        new_string += 'J'
    else:
        new_string += character

print(new_string)