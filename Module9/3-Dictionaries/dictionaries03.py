"""dictionaries03.py
Practical dictionary example.
"""

if __name__ == '__main__':

    # Initialize a dictionary of dictionaries
    creatures = {
        'Dinospore': {
            'kinds': ['nature'],
            'resilience': 117,
            'courage': 79,
            'willpower': 100,
            'determination': 69,
        },
        'Emberspark': {
            'kinds': ['fire'],
            'resilience': 77,
            'courage': 147,
            'willpower': 41,
            'determination': 87,
        },
        'Ripplefin': {
            'kinds': ['water'],
            'resilience': 84,
            'courage': 72,
            'willpower': 131,
            'determination': 33,
        },
    }

    # Iterate over outer dictionary
    for creature, data in creatures.items():
        print(creature)

        # iterate over inner dictionary
        for key, value in creatures[creature].items():
            print(f'\t{key}: {value}')

    # Create a list of all willpower values
    willpowers = [creatures[creature]['willpower'] for creature in creatures]
    print('willpowers:', willpowers)