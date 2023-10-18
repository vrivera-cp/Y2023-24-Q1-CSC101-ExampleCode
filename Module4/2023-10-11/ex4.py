"""ex4.py
An example of aliasing.
"""

animals = ['lion', 'tiger', 'bear']
dangerous = animals

dangerous.append('human')

print(animals)
print(dangerous)