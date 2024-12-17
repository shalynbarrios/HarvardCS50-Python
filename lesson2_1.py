# let's take a closer look at data types
# ----------------------------
# lists!
# ----------------------------

students = ["Hermione", "Harry", "Ron"]

# this is a list of 3 strings!

print(students[0])  # this prints the element at index 0 in the list `students`, which is the string "Hermione"

# to iterate through the list...
for student in students:  # this will iterate over the list and print each string.
    print(student)  # using the variable `student` to represent each element.

# if we need both the index and the value:
for i in range(len(students)):  # `range` expects an integer, so we use `len()` to get the length of the list.
    student = students[i]
    print(i, student)  # prints the index and the corresponding value at that index

# let's explore another data type
# ----------------------------
# dictionaries
# ----------------------------

# A dictionary is like a human dictionary:
# It maps something to something else (key-value pairs).
# In programming, a dictionary has keys and values. These pairs are called key-value pairs.

students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor",
    "Ron": "Gryffindor"
}

# we can access a value using its key:
print(students["Hermione"])  # prints the value associated with the key "Hermione", which is "Gryffindor"

# how can we loop through a dictionary?
# much like a list...

for student in students:
    print(student)  # this will print the keys of the stated dictionary

# to print both the key and the value:
for student in students:
    print(student, students[student])  # prints the key and its corresponding value

# alternatively, we can make it more readable:
for student in students:
    house = students[student]
    print(student, house)  # this stores the value in a variable
    # the key-value pair in this case is a student-house pair

# formatting the output to look prettier in the terminal:
for student in students:
    print(student, students[student], sep=", ")  # separates the key and value with a comma


# ----------------------------
# Let's consider the following problem
# ----------------------------

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Dog"}
]

# let's say we want to add a new student
# we will ask the user for the student's name, house, and patronus
# assume there is room for only two more students

room = 2

while room > 0: # check if there's room for a new student
    print(f"{room} room(s) left.")
    # prompt the user for the new student's details
    ask_name = input("What is the student's name? ")
    ask_house = input("What is the student's house? ")
    ask_patronus = input("What is the student's patronus? ")

    # Create a new student dictionary
    new_student = {
        "name": ask_name,
        "house": ask_house,
        "patronus": ask_patronus
    }

    # add the new student to the list
    students.append(new_student) # the append function is how we can add new items to a list

    # decrease the room count
    room -= 1 # remember, this is shorthand notation for room = room - 1
if room == 0:
    print("There are no more rooms left.")

# print the updated list of students
for student in students:
    print(student) # this should correctly print the former students and new students

# ----------------------------
# How can we add and replace values in a list?
# ----------------------------

# First, how do we add a new key-value pair?
# simple!
new_dict = {

}
new_dict["This is a new key"] = "This is the value"

print(new_dict)

# what if we wanted to replace a value in a key value pair?

new_dict["This is a new key"] = "This is a new value!"

print(new_dict)