"""dictionaries01.py
Examples of dictionary initialization.
"""

if __name__ == '__main__':

    # String keys with string values
    heroes = {
        'mario': 'A plumber that likes to jump.',
        'kirby': 'A pink marshmallow-like alien.',
        'samus': 'A bounty hunter with a spaceship.',
    }
    
    print(heroes)

    # Integer keys with string values
    course_numbers_to_names = {
        101: 'Fundamentals of Computer Science',
        202: 'Data Structures',
        203: 'Project-Based Object-Oriented Programming and Design',
    }

    print(course_numbers_to_names)
    
    # Alternative dictionary creation
    course_names_to_numbers = {}
    course_names_to_numbers['Fundamentals of Computer Science'] = 101
    course_names_to_numbers.update({'Data Structures': 202, 'Project-Based Object-Oriented Programming and Design': 203})

    print(course_names_to_numbers)

    # Can remove pairs using a key
    course_names_to_numbers.pop('Project-Based Object-Oriented Programming and Design')

    print(course_names_to_numbers)

    # A key can only exist once in a dictionary!
    heroes.update({'samus': 'A bounty hunter with a high-tech suit.'})

    print(heroes)

    # Keys must be "hashable"
    print(hash('mario'))
    print(hash('kirby'))
    print(hash('samus'))

    print(hash(101))
    print(hash(202))
    print(hash(203))

    print(hash('Fundamentals of Computer Science'))
    print(hash('Data Structures'))
    print(hash('Project-Based Object-Oriented Programming and Design'))

    # Values do not necessarily need to be hashable

    # This is entirely possible
    integers_to_lists = {
        0: [1, 2, 3],
        1: [4, 5, 6],
    }

    # Even though lists aren't hashable
    print(hash([1, 2, 3]))