# List Comprehension is a way to create lists using a concise syntax
# It allows us to generate a new list by applying an expression to each item in an existing iterable
arr = [2, 6, 4, 7]
result = [val * 2 for val in arr]
print(result)

print()
a = [4, 7, 5, 9, 2]
o = []
for val in a:
    o.append(val * 2)
print(o)

print()
res = [i ** 2 for i in range(10)]
print(res)

print()
matrix = [[1, 2], [3, 4], [5, 6]]
flatten = [val for row in matrix for val in row]
print(flatten)
