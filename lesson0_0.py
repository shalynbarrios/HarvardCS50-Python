print("hello there!")
# functions can have side effects
# if we had print("hello"
# it's missing the parenthesis
# very big deal to the computer!

# so to run code in vscode you say
# python (filename).py

print("What's your name? ")

input() # but input already has a built in
# paraameter to have a prompt
# input(prompt)

# this prompt is a string and input can only accept a string arguments

# so we can say

input("What's your name? ")

response = input("What's your name? ")
# the variable response hold's the input to the prompt 'What's your name?'

# the equals sign assignment

######

print("hello", response)

# When you want to combine strings (or other values)
#  with automatic spacing and support for non-string types 
# (e.g., numbers or objects).

print("hello" + response)

# What it does: The + operator concatenates strings directly without adding spaces. 
# Both "hello" and response must be strings, or you'll get an error (e.g., 
# if response is an integer, you'll need to convert it to a string with str()).

######

num = 4

print(2, num) # this is two arguments in the function print

# just lists these numbers

print(2 + num) # this is adding the two and then printing result
# this is one argument

# actually adds

###

# print automatically creates a new line
# you can override this behavior
# docs.python.org is the official python documentation

# print(*objects, sep =" ", end"\n", file=sys.stdout, flush = False)

# the name of this function is print
# everything inside of the function are the parameters

# objects* means that the function can take as many arguments as you want

# the next parameter is sep which is seperate
# when you pass in multiple arguments to print, there will be a
# " " a space, which is what something like print(2, num) does

# another parameter is end = '\n'
# \n means new line
# so we can override this

name = input("What's your name? ")

print("Hello, ", end = "")
print(name)
