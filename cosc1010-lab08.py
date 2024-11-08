# Grant Browning
# UWYO COSC 1010
# 11/07/2024
# Lab 08
# Lab Section: Austin
# Sources, people worked with, help given to:
# your
# comments
# here

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
rando_string = input("Please enter something:")

def Check_strings(check):
    if isinstance(rando_string, int):
        rando_string = int(rando_string)
        return rando_string
    elif isinstance(rando_string, float):
        rando_string = float(rando_string)
        return rando_string
    else:
        return False
    
print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound

def math_man(list):
    list = []
    return list

# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
mb = {m:"",b:""}
m = 0
b = 0
def rangelist(mb):
    if isinstance(mb, int):
        int(m) = mb{"m"} 
        int(b) = mb{"b"}
    if isinstance(mb, float):
        float(m) = mb{"m"} 
        float(b) = mb{"b"}
    else:
        return False

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
While True:
    if 
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
