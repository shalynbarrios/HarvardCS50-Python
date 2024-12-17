# Let's take a closer look at data
# specifically, lists

students = ["Hermione", "Harry", "Ron"]

# A list of 3 strings!

print(students[0])  # Prints the element at index 0 in the list `students`, which is "Hermione".

# Iterating through the list
for student in students:  # This will iterate over the list and print each string.
    print(student)  # Using the variable `student` to represent each element.

# If we need both the index and the value:
for i in range(len(students)):  # `range` expects an integer, so we use `len()` to get the length of the list.
    student = students[i]
    print(i, student)  # Prints the index and the corresponding value.

# Let's explore another data type: dictionaries (or "dicts")

# A dictionary is like a human dictionary:
# It maps something to something else (key-value pairs).
# In programming, a dictionary has keys and values. These pairs are called key-value pairs.

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor",
    "Ron": "Gryffindor"
}

# To access a value using its key:
print(students["Hermione"])  # Prints the value associated with the key "Hermione".

# How can we loop through a dictionary?

for student in students:
    print(student)  # This will print the keys.

# To print both the key and the value:
for student in students:
    print(student, students[student])  # Prints the key and its corresponding value.

# Alternatively, we can make it more readable:
for student in students:
    house = students[student]
    print(student, house)  # Stores the value in a variable for clarity.

# Formatting the output to look prettier in the terminal:
for student in students:
    print(student, students[student], sep=", ")  # Separates the key and value with a comma.


# Let's consider a list of dictionaries representing students

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Dog"}
]

# Let's say we want to add a new student
# We will ask the user for the student's name, house, and patronus
# Assume there is room for only one more student

room = 1

if room > 0:
    # Prompt the user for the new student's details
    ask_name = input("What is the student's name? ")
    ask_house = input("What is the student's house? ")
    ask_patronus = input("What is the student's patronus? ")

    # Create a new student dictionary
    new_student = {
        "name": ask_name,
        "house": ask_house,
        "patronus": ask_patronus
    }

    # Add the new student to the list
    students.append(new_student)

    # Decrease the room count
    room -= 1

# Print the updated list of students
for student in students:
    print(student)

# what if we wanted to replace a value in a key value pair?