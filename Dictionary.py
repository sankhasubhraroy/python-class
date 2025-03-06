# {
#     "Name": "Test",
#     "Age": "45",
#     "Location": "UK"
# }
# The above example is a JSON value

# Dictionary is a data structure that stores the value in key:value pairs
# Dictionary keys are case-sensitive
# Dictionary keys must be unique

# First method to declare a dictionary
customer = {
    "name": "Test Customer 1",
    "email": "test1@gmail.com",
    "age": 34,
    "address": {
        "country": "India",
        "state": "WB",
        "pincode": 764423
    }
}

print(customer)
# Accessing Dictionary Items Method 1
print(customer.get("name"))
# Accessing Dictionary Items Method 2
print(customer["email"])

# Another method to declare a dictionary
customerDictionary = dict(name="Test Customer 2", email="test2@gmail.com", age=27)

print(customerDictionary)
print(customerDictionary.get("name"))
print(customerDictionary["email"])

# Adding new Items to Dictionary
customerDictionary["phone"] = "9812738123"
print(customerDictionary)

# Updating existing item to Dictionary
customerDictionary["age"] = 45
print(customerDictionary)

# Removing Dictionary Items Method 1
customerDictionary.pop("phone")
print(customerDictionary)

# Removing Dictionary Items Method 2 (Removes the last key value pair)
customerDictionary.popitem()
print(customerDictionary)

# Clearing Whole Dictionary
customerDictionary.clear()
print(customerDictionary)

# We can Iterate through a Dictionary using for loops

# If we iterate through a dictionary by default keys will be fetched
# keys function convert the dictionary into a list containing the keys
# print(list(customer.keys()))
for key in customer.keys():
    print(key)

# Iterating through a dictionary value
# values function convert the dictionary into a list containing the values
# print(list(customer.values()))
for value in customer.values():
    print(value)

# Iterating through both keys and values
# items function convert the dictionary into a 2d list containing keys and values
# print(list(customer.items()))
for key, val in customer.items():
    print(f"The key: {key} => The value: {val}")
