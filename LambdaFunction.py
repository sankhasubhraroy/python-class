# Lambda Function means that the function without a name (Anonymous function)
# def keyword is used to define normal function - lambda keyword lambda keyword is used to define lambda function

st = "Hello, this is Python"

# Lambda function to convert a string to uppercase
toUpper = lambda s: s.upper()

print(toUpper(st))

# Lambda function to tell if its positive or negative
isPositive = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(isPositive(8))
print(isPositive(-8))
print(isPositive(0))

# Lambda function t return the square
square = lambda x: x ** 2

print(square(7))
print(square(17))

# Lambda function for multiply
mult = lambda x, y: x * y

print(mult(2, 7))
print(mult(5, 25))
