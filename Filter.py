# The Filter method filters the given iterables with the help of a function
# The Filter function test every element in the iterable (true or false) and then return true elements

def even(n):
    return n % 2 == 0


randomList = [5, 8, 66, 3, 45, 78, 33, 13, 24, 56]
filteredList = list(filter(even, randomList))

print(filteredList)

randomList = [34, 7, 9, 4, 77, 33, 65, 39]
filteredList2 = list(filter(lambda x: x % 2 == 0, randomList))

print(filteredList2)
