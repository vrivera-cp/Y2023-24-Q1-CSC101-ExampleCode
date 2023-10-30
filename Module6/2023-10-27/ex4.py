"""ex4.py
An example of aliasing and mutability.
"""
from ex2 import Cat

if __name__ == '__main__':
    mochi = Cat('Mochi', 6)

    harvest = mochi

    harvest.name = 'Harvest'
    harvest.age -= 1

    print("mochi:")
    print("\tname:", mochi.name)
    print("\tage:", mochi.age, '\n')

    print("harvest:")
    print("\tname:", harvest.name)
    print("\tage:", harvest.age)
