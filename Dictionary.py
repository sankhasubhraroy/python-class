# {
#     "Name": "Test",
#     "Age": "45",
#     "Location": "UK"
# }
# The above example is a JSON value

customer = {
    "name": "Test Customer 1",
    "email": "test1@gmail.com",
    "age": 34
}

print(customer)
print(customer.get("name"))

customerDictionary = dict(name="Test Customer 2", email="test2@gmail.com", age=27)

print(customerDictionary)
print(customerDictionary.get("name"))
