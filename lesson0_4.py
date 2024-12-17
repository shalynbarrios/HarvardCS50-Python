# onto functions! as in, making our own :)

name = input("What's your name? ")

def hello(name: str) -> None:
    greeting = "Hello " + name
    print(greeting)

hello(name)

# the `name` parameter in the function and the `name` variable outside it are separate because of scope.
# variables defined outside a function exist in the global scope and are accessible anywhere in the program.
# function parameters and variables inside a function exist in the local scope of that function 
# and are independent of global variables, even if they share the same name!
# in this case, the global `name` is passed as an argument to the function's local `name` parameter,
# so they are two different variables, not the same one.

name = input("What's your name? ")

def hello(person: str) -> None: # `person` is the local parameter.
    greeting = "Hello " + person
    print(greeting)

hello(name)
# this is easier to see
# the variable name gets copied into the parameter person

def hello() -> None:
    name = input("What's your name? ")
    print(f"Hello {name}")

hello()
# this is even better

def hello(name: str) -> None:
    print(f"Hello {name}")

user_name = input("What's your name? ")
hello(user_name)
# but this is my favorite :)

# remember we can give our functions default values
def hello(name: str = "world") -> None: # so no argument, by default it will say Hello world
    print(f"Hello {name}")

user_name = input("What's your name? ")
hello(user_name)


### 

# but if you have to keep scrolling up to define functions before you can 
# use them... it's easy to lose track where you are
# but there is a solution!

def main():
    name = input("What's your name? ")
    hello(name)

# we have't called this function main() yet
# which is good because it would raise an error about hello() not
# being defined just yet

def hello(name: str = "world") -> None:
    print("hello", name)

main() # by the time we call our main function, hello() is already defined
# so python won't throw an error and instead
# refer to the function it read earlier

# however! let's talk about scope more then

def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("hello", name)

main()

# THIS WILL RETURN AN ERROR
# scope refers to existing in only the context in which you defined it
# name was locally defined within a function called main()
# the function hello() cannot access it

# it CAN access it by...
# 1. Passing `name` as an argument to hello():
# 2. Defining `name` in the global scope. HOWEVER, this is generally not recommended 

# The first approach (passing variables as arguments) is a better practice in most cases.

# like this:
def main():
    name = input("What's your name? ")
    hello(name)  # Pass the value of `name` to hello(person) as an argument

def hello(person): # the function now accepts a parameter
    print("Hello", person) # this prints the value of the parameter `person`

main()

###

# wonderful! now let's use this and practice returning values

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(num):
    return num*num # or n**2 OR pow(n, 2)

main()