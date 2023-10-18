"""ex5.py
Examples of copying a list.
"""

animals = ['lion', 'tiger', 'bear']
dangerous = list(animals)
# or dangerous = animals[:]

dangerous.append('human')
# or dangerous = animals + ['human']

print(animals)
print(dangerous)