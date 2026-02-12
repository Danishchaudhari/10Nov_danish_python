#Writing a Python program to demonstrate how to access values in a dictionary using keys.

dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer",
    "hobby": "Photography",
    "is_student": False
}

print(dict)

# Accessing value using key

print("Name:", dict["name"])
print("Age:", dict["age"])
print("City:", dict["city"])
print("Job:", dict["job"])
print("Hobby:", dict["hobby"])
print("Is Student:", dict["is_student"])