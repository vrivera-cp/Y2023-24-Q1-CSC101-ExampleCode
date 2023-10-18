"""ex2.py
An example of importing classes.
"""
import ex1
from ex2 import Cat

if __name__ == '__main__':
    mochi = ex1.Cat()
    mochi.name = 'Mochi'
    mochi.age = 6

    harvest = Cat('Harvest', 5)

    print("Type of mochi variable:  ", type(mochi))
    print("Type of harvest variable:", type(harvest))

    print("type(mochi) is type(harvest): ", type(mochi) is type(harvest))
