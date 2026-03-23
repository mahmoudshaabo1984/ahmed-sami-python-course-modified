

person = {
    "first_name": "ahmed",
    "last_name": "sami",
    "age": 31 
}
# print(person["first_name"])
# print(person.get("last_name"))

#  Constructor
# person2 = dict(f_name="sara", l_name="wileam")
# print(person2)


# #add
person["phone"] = "12345678"
print(person)

# Displaying dictionary keys
print(person.keys())


# Displaying dictionary items
# print(person.items())

# Creating a copy of 'person' dictionary 
person3 = person.copy()

#the addition of the "city" key
person3["city"] = "cairo"
# Removing the "city" key from 'person3'
del person3["city"]
# Removing the "phone" key from 'person
person.pop("phone")
# Getting the length (number of items) of 'person3'
print(len(person3))
print(person3)

#  Clearing all items from the 'person' dictionary
# person.clear()
# print(person)

# List of dictionaries, where each dictionary represents a person
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

# Accessing the name of the second dictionary in the list
print(people[1]['name'])  # Prints 'Kevin'
