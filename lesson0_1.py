name = input("What's your name? ")
print("hello, ", end = "") # no new line
print(name)

# what about passing something differnt for the seperate parameter

name = input("What's your name? ")
print("hello", name, sep = "_") # this will seperate
# the arguments with _
# essentially replaces the comma

# by the way, these are positional parameters
# the frst thing you pass to print gets printed first
# the second thing you pass to print gets printed second

# there are also named parameters 
# such as end = and sep =
# they are optional
# and you use them by name, by calling on them

###

# anyways, let'sa say you want to use double quotes
# or you are expecting an input with double quotes

print('hello, "friend"')

# or

print("hello, \"friend\"") # backslash is "escaping"