# --------
# Introduction to Python
# --------
# Hi everyone!
# This is a collection of files to help guide you through Harvard's CS50 Intro to Python course
# I recommend following Professor Malan as you skim through this guide
# I start numbering with zero-based lessons, which will make sense why I did this mini-easter-egg once you know what lists are.
# For now, interpret "Lesson 0" notes as Lecture 1 guide.

# --------
# Introduction to Printing
# --------
print("Hello there!")
# Functions can have side effects.
# For example, if we had print("Hello" (missing the closing parenthesis),
# it would cause an error. This is a big deal to the computer!

# --------
# Running Python Code
# --------
# To run your code in VS Code, use the following command in the terminal:
# python (filename).py

# --------
# Using Input to Get User Data
# --------
print("What's your name? ")

input()  
# The `input()` function already has a built-in parameter to include a prompt.
# Syntax: input(prompt)

# The prompt must be a string because `input()` only accepts strings as arguments.

# Example with a prompt:
input("What's your name? ")

# Assigning the user's input to a variable:
response = input("What's your name? ")  
# The variable `response` holds the input provided by the user.

# --------
# Printing with Variables
# --------
print("Hello", response)  
# The `print()` function can handle multiple arguments.
# It automatically adds a space between them.

print("Hello" + response)  
# Using the `+` operator concatenates strings directly, without spaces.
# Both "Hello" and `response` must be strings. If `response` isn't a string
# (e.g., it's a number), you must convert it using `str()`.

# --------
# Numbers and Operations
# --------
num = 4

print(2, num)  # Outputs: 2 4 (two arguments separated by a space).
# This just lists the numbers.

print(2 + num)  # Outputs: 6 (adds the numbers before printing).
# This performs addition.

# --------
# Customizing Print Behavior
# --------
# By default, `print()` automatically creates a new line after output.
# You can override this behavior using the `end` parameter.

name = input("What's your name? ")

# Example: Printing without a newline
print("Hello, ", end="")  # Overrides the default new line.
print(name)  # Continues on the same line.

# --------
# Exploring the Print Function
# --------
# `print()` has several parameters:
# print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)

# - `*objects`: Accepts multiple arguments (e.g., print(2, num)).
# - `sep`: Defines the separator between arguments (default: a space).
# - `end`: Determines what happens after the output (default: new line `\n`).
# - `file`: Specifies the output file (default: sys.stdout).
# - `flush`: Forces immediate output (default: False).

# For example, when passing multiple arguments to `print()`:
# print(2, num) will separate the numbers with a space because `sep=" "` by default.

# You can also override `end` to avoid the automatic new line.

# --------
# Reference
# --------
# For more info, check the official Python documentation:
# This is VERY helpful!!
# https://docs.python.org

