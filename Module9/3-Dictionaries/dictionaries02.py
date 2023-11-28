"""dictionaries02.py
Examples of accessing dictionaries.
"""

if __name__ == '__main__':

    # Initialize a dictionary
    heroes = {
        'mario': 'A plumber that likes to jump.',
        'kirby': 'A pink marshmallow-like alien.',
        'samus': 'A bounty hunter with a spaceship.',
    }

    # Values are accessed using the bracket operator and keys
    print(heroes['mario'])
    print(heroes['kirby'])
    print(heroes['samus'])

    # "indices" don't exist
    try:
        print(heroes[0])
    except KeyError:
        print("Invalid key!")

    # For loops iterate on dictionary keys
    for key in heroes:
        print(key)

    for key in heroes:
        print(heroes[key])

    # Can iterate on both keys and values
    for key, value in heroes.items():
        print(f'{key}: {value}')