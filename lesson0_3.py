# integers are whole nums
# + - * / % 

# if you put python in the terminal
# it calls python interpreter
# so you can ask math questions like 1 + 1
# it's interactive!

x = int(input("insert a num"))
y = int(input("what's the next"))

z = x + y
print(z)

# if we did...

x = input("insert a num")
y = input("what's the next")

z = x + y # you are concatenating two strings b/c the
# input function returns a string
print(z)

# or...

x = int(input("insert a num")) # inner function value becomes the argument to the outer function
y = int(input("what's the next"))

print(x + y)