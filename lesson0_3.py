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

# to floats..

x = float(input("insert a num")) # inner function value becomes the argument to the outer function
y = float(input("what's the next"))

print(int(x + y))

# there is a function called round

# round(number[, ndigits]) these are the available parameters
# only tkaes one number (no star)
# [] square brackes mean something optional
# if you wanted to round to the 100th place, that would be 2
# 2 decimal places

x = float(input("insert a num")) 
y = float(input("what's the next"))

print(round(x + y))

# what about making 1000 to 1,000? the comma convention?

x = float(input("insert a num")) 
y = float(input("what's the next"))

z = round(x+y)

print(f"{z:,}")

### here is more rounding practice

x = float(input("insert a num")) 
y = float(input("what's the next"))

z = round(x/y, 2) # this second arument says "give us two decimal places"

print(z)

# we can rewrite the exact same code by

x = float(input("insert a num")) 
y = float(input("what's the next"))

z = x/y

print(f"{z:.2f}")
