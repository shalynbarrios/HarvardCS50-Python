name = input("What's your name? ")

print(f"Hello, {name}") # f string is  a format string
# format stuff in the string in a special way

# strings themselves come with a lot of customizing and functionality
# we can clean it up or reformat it

# remember strings are a datatype


# ask user for name
name = input("What's your name? ")

# remove whitespace from string
name = name.strip() # method
# if name is a string, we can use some built-in methods
# strips space from left and right
# so this line will assign/update as the new value

# capitalize user's input
# name = name.capitalize()

# capitalize user's input (this one is better if multiple words that need capitalization)
name = name.title()

# say hello to user!
print(f"Hello, {name}")

# BTW! In a terminal, just press the up arrow
# to repeat your previous call

####

# you can also do

name = input("What's your name? ").strip().title()
# remember, a method is a function that is built in to a type of value (strings)

# saves two lines

print(f"Hello, {name}")

####

# What if we have both the first and last name?

# ask user for name
name = input("What's your name? First and last ").strip().title()

# split user's name into first name
first_name, last_name = name.split(" ") # passing in the argument " " space to indicate
# that i want to split the string at the space
# this returns two substrings

# say hello to user
print(f"Hello, {first_name}")