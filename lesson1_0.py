# conditionals !

# conditional statements are a way to ask the
# computer some questions! (make the computer do a set of commands whether or not something is true)

# > , >= , < , <= , == , !=

# if, elif, else

# suppose we want to compare some integers

x = int(input("One num please: "))
y = int(input("One num please: "))

if x < y: # if (boolean expression (ie true or false question))
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x is equal to y")

# but this is repetititve and asks the cumputer 3 questions (that might not be necessary)
# if we already know for example x == y, then x is certainly not greater than y
# so we are waisting work my still asking it
# because they are mutually exclusive

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: # if the two previous ones are false, then this means x is equal to y
    print("x is equal to y")

###

# let's introduce keyword or

# is x equal to y or not?

if x < y or x > y:
    print("x is not equal to y")

# a better way to ask this without using the or keyword

if x == y:
    print("x is equal to y")

###

# let's introduce keyword and

score = int(input("Score?"))

if score >= 90 and score <=100: # you can also say.. 90 <= score <= 100:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 60:
    print("F")

# remember, if, elif, and else are mutually exclusive
# meaning once one logic is true the others will not run

###

# parity (is a number even or odd)
# % not a percentage (it's to calculate remainder)
# Example: 4 % 3 = 1 (4 divided by 3 leaves a remainder of 1)

x = int(input("num?"))

# Even numbers have no remainder when divided by 2

if x % 2 == 0:
    print("even")
else: 
    print("odd")

# let's make it a function!

num = int(input("check a num's parity")) # ideally this should be in the main function

def main():
    print("hello world")
    check_parity(num) # calls the `check_parity` function for the argument num


def check_parity(n: int) -> None: # passes in the value of num in the parameter n
    if n % 2 == 0:
        print("even")
    else: 
        print("odd")

main()

# OR

def main():
    x = int(input("What's the x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    return n % 2 == 0


# since we are a little more ahead of what this course is currently at,
# professor is talking about truthy falsy

my_list = [1,2]

if my_list: # this is a bool expression going to return true
    print("This is checking that the list has elements and is not empty.")

## new keyword!!

# match

name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
else:
    print("Who?")

# how can we make this better?

gryffindor_name_list = ["Harry", "Ron", "Hermione"]

if name in gryffindor_name_list:
    print("Gryffindor")
else:
    print("Who?")

# okay! now let's try the new match keyword

# name = input("What's your name? ")

# match name: this is a new function in python 3.10
#     case "Harry" | "Ron" | "Hermione":
#         print("Gryffindor")
#     case _: the underscore tells python this is a catchall statement
#         print("who?")