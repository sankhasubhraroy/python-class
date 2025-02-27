# The Reduce function is used to apply a particular function passed in its arguments to all the list elements
from functools import reduce


def add(x, y):
    return x + y


a = [1, 2, 3, 4, 5]
result = reduce(add, a)

print(result)

b = [2, 4, 6, 8, 10]
result2 = reduce(lambda x, y: x * y, b)

print(result2)
