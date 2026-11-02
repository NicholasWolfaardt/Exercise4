# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apples", "bananas", "grapes", "pineapple", "cucumber"]

# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
  print(fruit)


#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
num = 5
while num > 0:
  print(num)
  num -= 1


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1,11):
  print(i**2)


#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random

# TODO: Create a list of colors
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# TODO: Use a for loop to select and print 3 random colors from the list
for i in range(0, 3):
    print(colours[random.randint(0, 6)])


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions


# TODO: Use a while loop to create a simple calculator
