# Loops in Python!

# to create a new Python file say code (name) in the terminal
# to run the code say python (name)

# ----------------------------
# the 'while' loop
# ----------------------------

# example 1: counting down
i = 3
while i > 0:
    print("meow")
    i -= 1

# example 2: counting up
i = 0
while i < 3:
    print("meow")
    i += 1

# ----------------------------
# intro to 'for' loops and lists
# ----------------------------

# lists are another data type in Python used to store multiple items.

# Using a list
for meow in [0, 1, 2]:  # conventionally, 'i' is used when you need the index
    print("meow")

# using the 'range' function
for meow in range(3):  # 'range' expects one argument and generates numbers 0 to n-1
    # remember, range starts from 0 and does not include the argument
    print("meow")

# example 3: using an underscore (_) for unused variables and you don't need the index
for _ in range(3):  
    print("meow")

# example 4: using string multiplication
print("meow\n" * 3, end="")  # multiplies the string and removes the trailing newline

# ----------------------------
# asking the user for input
# ----------------------------

# ask the user how many times to meow
ask = int(input("How many times should this cat meow? "))
while ask > 0:
    print("meow")
    ask -= 1

# example 2: Using a 'while True' loop for input validation
# THIS is a very common solution when you want to keep asking the user
# until they provide a valid input.
while True:
    n = int(input("How many times should this cat meow? "))
    if n > 0:  # exit the loop if the input is valid
        break

# using the validated input
for _ in range(n):
    print("meow")

# ----------------------------
# meow as a function!
# ----------------------------

# a simple meow function
def main():
    meow(3)  # call the meow function with 3 as an argument

def meow(n: int) -> None:  # type hints: 'n' is an integer, and the function returns None
    for _ in range(n):  # use a for loop to print 'meow' n times
        print("meow")

main() # calls main() function

# example 2: another way we can write this function is by breaking it into smaller functions
def main():
    number = get_number()  # get a valid number from the user
    meow(number)  # call the meow function with the number

def get_number() -> int:
    # below is a very common solution to keep asking until the user gives
    # a value that meets your criteria.
    while True:
        n = int(input("How many times should this cat meow? "))
        if n > 0:  # ensure the number is positive
            return n  # return the valid number

def meow(n: int) -> None:
    for _ in range(n):  # print 'meow' n times
        print("meow")

main()

# ----------------------------
# edge case: range w/ zero
# ----------------------------

# note that if 'range(0)' is used, the loop body won't execute at all.
for _ in range(0):
    print("This will never print!")



