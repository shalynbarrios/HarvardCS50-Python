# let's look closer at lists

students = ["Hermione", "Harry", "Ron"]

# list of 3 strings!

print(students[0]) # going to print element 0 in the list students which is Hermione

for student in students: # this will iterate and print the strings over the list
    print(student) # we are using the variable so let's not call it _

# if we need the index

for i in range(len(students)):
    student = students[i]
    print(i, student)