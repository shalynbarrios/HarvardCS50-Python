# welcome back, everyone!

# Today, we’ll do something fun inspired by the famous Super Mario Nintendo game
# We're going to create the columns of bricks that Mario has to jump over.
# We will be doing this with hashtags to represent a block (one hashtag = one block)
# It might not be the most visually appealing haha, but let's explore how to solve this!

# example: If we want a brick 3 blocks tall, we could do this:

print("#")
print("#")
print("#", end="\n" * 2)  # This ensures the blocks aren't stacked together in the terminal.

# However, this method isn't very efficient.
# Why? Good question! If we wanted a block that was 50 bricks high.. we'd have to run the print function 50 times
# it's important to think of extremes when constructing a good program... and you probably don't want to copy/paste 50 times

# String multiplication is another good idea! However, this doesn't work as intended for VERTICAL columns:
print("#" * 3, end="\n" * 2)

# Can you think of a way to solve this using string multiplication? 
# Hint: It’s great for rows (HORIZONTAL), not columns. We will come back to this later. Good idea though!

# Alternatively, we can use loops:

for _ in range(3):  # The underscore ( _ ) is used when the variable won't be reused.
    print("#") # we are not using the variable as you can see

# However, if you’re not comfortable with `_`, you can use a descriptive variable:

for brick in range(3): 
    print("#")
print(" ")  # this creates an empty line for separation.

# The good thing about this loop is that if we wanted to ask the user how big this block should be,
# we can use the input() function and pass in the response as an integer which can then be the argument for range().

bricks = int(input("How tall should this block be? "))

for brick in range(bricks): 
    print("#")
print(" ")

# For now though, let's stick to set numbers (3)

# Let’s make this process more reusable by creating our own function:

def main():
    print_column(3)  # 3 is the argument for the `height` parameter.

def print_column(height: int) -> None:  # using type hints for clarity, this is a good habit to build
    for _ in range(height):
        print("#")
    print()  # adds a line for aesthetic separation

main()

# Alternatively, we can simplify the function further:

def main():
    print_column(3)

def print_column(height: int) -> None:
    print("#\n" * height)

main()

# ----------------------------
# Horizontal Rows: Mario’s Golden "?" Blocks
# ----------------------------
# Let’s switch gears to horizontal rows, like Mario’s golden "?" blocks:

def main():
    print_row(4)

def print_row(width: int) -> None:
    print("?" * width)
    print()

main()

# ----------------------------
# Creating 2D Blocks
# ----------------------------
# Now, how about creating a chunk of a block, like the ones Mario runs on?

def main():
    print_square(3, 3)  # 3x3 square.
    print_square(5, 5)  # 5x5 square.

def print_square(height: int, width: int) -> None:
    x_length = "#" * width
    for _ in range(height):
        print(x_length)
    print()

main()

# Another way to approach this:

def main():
    print_square(3)
    print_square(5)

def print_square(size: int) -> None:
    # For each ROW in the square:
    for i in range(size):
        # For each BRICK in the row:
        for j in range(size):
            print("#", end="")  # Prevents a new line after every brick.
        print()  # starts the next row once the iteration of the nested loop is complete

main()

# Comparing the two approaches:
# - The first function uses two parameters: width and height. 
#      this allows users to create rectangles, e.g., a 3x4 or 5x7 block.
# - The second function assumes the block is a square (equal width and height, like 3x3, 5x5).

# Simplifying the second function further:

def main():
    print_square(3)
    print_square(5)

def print_square(size: int) -> None:
    for row in range(size):  # Loop creates each row
        print("#" * size)  # We can then generate the row by string multiplication

main()

# this function also assumes the block is a square with equal dimensions.