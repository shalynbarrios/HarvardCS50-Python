# Introduction to Exceptions

# ----------------------------
# What are Exceptions?
# ----------------------------

# Exceptions in programming refer to something "Exceptional"
# However, unlike in the English language, being Exceptional is not a good thing!
# Except = Something has gone wrong

# print("Hello, world)
# This will raise a SyntaxError
# Specifically--"SyntaxError: unterminated string literal (detected at line 7)"

# Let's break down what SyntaxError means by splitting it into two pieces
# Well the word "error" you should know what that means
# But how about the word syntax?

# You can think of syntax as Python's grammar. Actually, any programming language's grammar
# So, a "SyntaxError" means that there's something wrong in the "grammar" of your code
# i.e. you didn't write the code correctly and Python is having trouble understanding what you
# are trying to say

# "unterminated string literal" means you started something you didn't stop
# in this case a string
# so it's like saying "you literally didn't finish the string"

# so to fix this, let's "terminate" the string by ending it with a "
print("Hello, world")

# ----------------------------
# Runtime Errors
# ----------------------------

# Let's try something

x = int(input("What is x? ")) # this is passing the return value of the input and "making" it into an integer

print(f"x is {x}") # This will print an f-string, which will subsitute the value of x into {x}

# All seems to be well when we type in a number like 50 or 200
# But think about corner cases -- in other words, "what could go wrong?"

# If what the user types is NOT an integer
# Python cannot convert such into an integer

# For example, if the user types in the string "cat"
# How could you even convert that into a whole number (int)? You can't.
# This is a Runtime Error -- specifically, a ValueError

print(f"x is {x}") # If we run this code and type the string "cat"
# We get the following error in the terminal:
# "ValueError: invalid literal for int() with base 10: 'cat'"

# What does this mean?
# Well, it's not a SyntaxError because the code's 'grammar' isn't incorrect

# It's an error with a value
# It's a value we didn't expect would be passed through
# The error message is telling us that what we passed through int() was invalid

# So how can we go about fixing this?
# We can tell the user to only type numbers, but obviously, someone might not read the instructions
# So we can't 100% trust that every human will type numbers

# So that's not too effective
# We have to do something with the code that will handle potential errors

# ----------------------------
# Error Handling: Try and Except
# ----------------------------

# Turns out, there are these two built-in blocks in Python that are error-handling
# We use these blocks like this:

try: # Python will try to run this code
    x = int(input("What is x? "))
    print(f"x is {x}")
except: # Except if the code fails, then this code will run
    print("x is not a number")

# However, we can tell Python if there's a specific error we can anticipate
# And therefore, should run specific code

try:
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError: # except when a ValueError occurs when we tried to run the previous code, run the following code:
    print("x is not a number") # and so here we are giving the user an appropriate message in the terminal

# This is much better than our previous code
# However, we can make this better

# The "try" block should generally only have lines of code that you think might fial
# The print() function we've used many times before and is not going to raise an error
# So we can take that out of our try block

try:
    x = int(input("What is x? "))
except ValueError:
    print("x is not a number")
print(f"x is {x}")

# Unfortunately, this raises another error
# "NameError: 'x' is not defined"

# But Shay, didn't we define x on line 95?

# If you have a bit of experience programming, you might say it's the scope that caused this error
# However, this is not the case
# Remember that x is assigned the int() of the value of the input function
# But when something is going wrong (i.e. "cat") then there is no value for x to be equal to
# And since 'print(f"x is {x}")' is always going to run no matter if we tried and succeeded or tried and failed, there will be an error

# Even though we see that x = int(input("What is x? ")), it's not being evaluated as such for when the input is a string
# So how do we fix this?

try:
    x = int(input("What is x? "))
except ValueError:
    print("x is not a number")
else: # this will only run if nothing exceptional happened / the except block was not triggered!
    print(f"x is {x}") # so if you try and succeed, this line of code will now run

# the else block makes it mutally exclusive
# so that if we try AND succeed, the else block will run

# Let's make this a bit more user friendly
# What if the user typed a string by mistake?
# Let's ask them to input an integer again and again until they finally do
# Well what might we use to prompt something over and over?
# Loops!

while True:
    try:
        x = int(input("What is x? "))
        break # so if the code above works, we will quit prompting the user over and over again by exiting the loop and continue with our code
    except ValueError:
        print("x is not a number") # if the user keeps inputing something that is not an integer, this code will keep printing as a result

print(f"x is {x}") # This won't raise an error like it did before
# Why? Because to exit out the loop to reach this line of code is to say that the input must have been a number
# Otherwise the program would keep looping until it breaks
# And it only breaks when 'x = int(input("What is x? "))' runs correctly

# This is great control flow (flow of logic)

# If the user types in something that can be converted into an integer, then great!
# nothing "exceptional" happens
# If the user does type in let's say a string "cat"
# The user will informed that x is not a number
# and prompted again the question "What is x? "

# Unfortunately for the user (fortunately for us so the code doesn't break) they will be stuck in an infinite loop if they refuse to provide a number
# And that's a good thing! It prevents hackers (or people who try to find ways to make code break) from breaking out code and causing errors

# Suppose that we want to run this code quite often
# Let's make it into a function!

# ----------------------------
# Functions with Try and Except
# ----------------------------

def main():
    value_of_get_int = get_int()
    print(f"x is {value_of_get_int}")

def get_int() -> int:  # Type hint indicates the function returns an integer
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print("x is not a number")
    return x # this will return what x is after the loop breaks

main()

# We can write this more concisely 

def main():
    value_of_get_int = get_int()
    print(f"x is {value_of_get_int}")

def get_int() -> int:  # Type hint indicates the function returns an integer
    while True:
        try:
            x = int(input("What's x? "))
            return x # The return statement exits the loop AND returns a value, so we no longer need the break statement
        except ValueError:
            print("x is not a number")

main()

# More so...

def main():
    print(f"x is {get_int()}")

def get_int() -> int:
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not a number")

main()

# Let's say you didn't want to keep telling the user "x is not a number"

# ----------------------------
# The Pass Statement
# ----------------------------

# You want to catch an error but you don't want to print anything?
# Well you can pass and essentially carry on

def main():
    print(f"x is {get_int()}")

def get_int() -> int:
    while True:
        try:
            return int(input("What's x? (x should be a number) "))
        except ValueError:
            pass # Still catching it! But I'm still in the loop

main()

# Here are some final refinements

def main():
    print(f"x is {get_int("What's x?")}")

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()

# ----------------------------
# Diffference between Break, Pass, Continue
# ----------------------------

# Just to recap, this is the break statement

while True:
    x = input("Type 'stop' to exit: ")
    if x.lower() == "stop":
        print("Loop stopped!")
        break  # Exit the loop
    print(f"You typed: {x}")

# This is the pass statement

for i in range(5):
    if i == 2:
        pass  # Placeholder, does nothing for this condition
    print(i)

# A lot of students question why the pass statement exists if it does absolutely nothing!
# And that is a great question. Remember, the pass statement is a placeholder
# And recall that empty functions are not allowed in Python

# But let's say you are sketching out a piece of your program but haven't quite figured out the logic yet

def function_i_am_working_on():
    pass

# This way, you can have an "empty" function ready for when you have figured out the logic you need to type in instead!

# This is the continue statement

for i in range(5):
    if i == 2:
        continue  # Skip the rest of this iteration
    print(i)

# The continue statement is for when you want to skip specific cases but want to remain in the loop and not break out of it entirely

for number in range(1, 11):  # Loop through numbers 1 to 10 (remember, loops count up to but not including)
    if number % 2 == 0:  # Skip even numbers
        continue # this continue statement prevents the iteration from reaching the print function
    print(f"Odd number: {number}")

# ----------------------------
# Summary
# ----------------------------

# Exceptions occur when something goes wrong in code execution (e.g., ValueError, SyntaxError).  
# Use try-except to handle errors gracefully and avoid program crashes.  
# Loops with try-except can ensure valid user input (e.g., int only as we saw today).  
# Break exits loops, continue skips iterations, and pass acts as a placeholder (commonly used for functions).  
