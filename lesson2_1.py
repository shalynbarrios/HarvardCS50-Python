# Let's take a closer look at data types

# ----------------------------
# Lists!
# ----------------------------

students = ["Hermione", "Harry", "Ron"]

# This is a list of 3 strings!

print(students[0])  # This prints the element at index 0 in the list `students`, which is the string "Hermione".

# To iterate through the list...
for student in students:  # This will iterate over the list and print each string.
    print(student)  # Using the variable `student` to represent each element.

# If we need both the index and the value:
for i in range(len(students)):  # `range` expects an integer, so we use `len()` to get the length of the list.
    student = students[i]
    print(i, student)  # Prints the index and the corresponding value at that index.

# ----------------------------
# Dictionaries
# ----------------------------

# A dictionary is like a human dictionary:
# It maps something to something else (key-value pairs).
# In programming, a dictionary has keys and values. These pairs are called key-value pairs.

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor",
    "Ron": "Gryffindor"
}

# We can access a value using its key:
print(students["Hermione"])  # Prints the value associated with the key "Hermione", which is "Gryffindor".

# How can we loop through a dictionary?
# Much like a list...

for student in students:
    print(student)  # This will print the keys of the stated dictionary.

# To print both the key and the value:
for student in students:
    print(student, students[student])  # Prints the key and its corresponding value.

# Alternatively, we can make it more readable:
for student in students:
    house = students[student]
    print(student, house)  # This stores the value in a variable.

# Formatting the output to look prettier in the terminal:
for student in students:
    print(student, students[student], sep=", ")  # Separates the key and value with a comma.

# ----------------------------
# Let's consider the following problem
# ----------------------------

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Dog"}
]

# Let's say we want to add a new student.
# We will ask the user for the student's name, house, and patronus.
# Assume there is room for only two more students.

room = 2

while room > 0:  # Check if there's room for a new student.
    print(f"{room} room(s) left.")
    # Prompt the user for the new student's details.
    ask_name = input("What is the student's name? ")
    ask_house = input("What is the student's house? ")
    ask_patronus = input("What is the student's patronus? ")

    # Create a new student dictionary.
    new_student = {
        "name": ask_name,
        "house": ask_house,
        "patronus": ask_patronus
    }

    # Add the new student to the list.
    students.append(new_student)  # The `append` function is how we can add new items to a list.

    # Decrease the room count.
    room -= 1  # Remember, this is shorthand notation for `room = room - 1`.

if room == 0:
    print("There are no more rooms left.")

# Print the updated list of students.
for student in students:
    print(student)  # This should correctly print the former students and new students.

# ----------------------------
# Adding and Replacing Values in a Dictionary
# ----------------------------

# First, how do we add a new key-value pair? simple!
new_dict = {}

new_dict["This is a new key"] = "This is the value"
print(new_dict)

# What if we wanted to replace a value in a key-value pair?
new_dict["This is a new key"] = "This is a new value!"
print(new_dict)

# What if we have a key-value pair but no value (perhaps yet)?
# ----------------------------
# None
# ----------------------------

# Let me introduce the None keyword.

# Example of None
x = None  # x is initialized with no value.
if x is None:
    print("x has no value!")

# The None keyword in Python represents the absence of a value or a null value.
# It is often used to initialize variables or indicate a function does not return anything.

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Dog"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}  # Draco does not have a patronus.
    # We can say "none" in English, but `None` lets Python know there is truly no value for this key.
]

for student in students:  # Will run through our list.
    print(student["name"])  # Within each iteration, we ask for the value of the key "name".

# What if we wanted the house of each student?

for student in students: 
    print(student["house"]) 

# What if we wanted the patronuses?

for student in students: 
    print(student["patronus"]) 

# I think you get the point - first we have to iterate through each element of the list,
# then we access the desired value with the key.

# What if we want to print the name, house, and patronus?
# As we discussed in Lesson 0, `print` can take multiple arguments.

for student in students: 
    print(student["name"], student["house"], student["patronus"], sep=", ") 

# At the end of the day, dictionaries are much like those in the real world.
# Instead of words to definitions, it's keys to values.

# ----------------------------
# Summary
# ----------------------------

# - Lists are ordered collections of elements.
# - Dictionaries map keys to values.
# - Nested data structures combine lists and dictionaries.
# - The None keyword signifies no value.