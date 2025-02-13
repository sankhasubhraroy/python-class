# Map function is used to apply a given function to every item of an iterable
# Map always return a new map object, so we need to convert it back to list
# map(function, iterable)


# Map for making element double
arr = [11, 5, 8, 6, 23]


def double(x):
    return x * 2


arr2 = list(map(double, arr))

print(arr2)

# Map for making element square
l = [4, 8, 2, 5]

result = list(map(lambda x: x ** 2, l))

print(result)

# Map for multiple iterables adding each element
a = [1, 2, 3, 4]
b = [4, 3, 2, 1]

res = list(map(lambda x, y: x + y, a, b))

print(res)
