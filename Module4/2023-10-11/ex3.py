"""ex3.py
An example of removing items from a list.
"""

animals = [
    'cat',
    'penguin',
    'giraffe',
    'alligator',
    'dolphin',
]

animals.pop() # returns 'dolphin'

animals.pop(0) # returns 'cat'

animals.remove('giraffe') # returns None

del animals[1] # removes 'alligator'

print(animals)