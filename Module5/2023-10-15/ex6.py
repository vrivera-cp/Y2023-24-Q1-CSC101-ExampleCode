"""ex6.py
An example of a non-pure function.
"""


def mutation_example(x: list[int], divisor: int) -> None:
    for i in range(len(x)):
        x[i] = x[i] % divisor


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    mutation_example(list1, 3)

    print(list1)

    list2 = [11, 12, 13, 14, 15]
    mutation_example(list2, 7)

    print(list2)
