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

def int_float_converter(num):
    """Check strings to see if they are an int or float, and convert them if so"""


    isNeg = False
    if "-" in num:
        isNeg=True
        num=num.replace("-","")
    if "." in num:
        num_split=num.split(".")
        if len(num_split)==2 and num_split[0].isdigit() and num_split[1].isdigit():
            if isNeg:
                return (-1)*float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isNeg:
            return (-1)*int(num)
        else:
            return int(num)
    else:
        return False

if int_float_converter(rando_string):
    print(f"This is a number")
else:
    print(f"This is not a number")    

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


def linearcomputation(x):
    """Create a function slope-intercept that takes in four parameters"""
    m = input("Please enter value for m:")
    b = input("Please enter value for b:")
    lower_bound = input("Please enter value for lower bound:")
    upper_bound = input("Please enter value for upper bound:")
    y_list = []
    if int_float_converter(m) and int_float_converter(b) and int_float_converter(lower_bound) and int_float_converter(upper_bound):
        if check_bounds():
            for i in range(lower_bound, upper_bound):
                y_list.append(m*i+b)
                return y_list
    else:
        print("Invalid input") #Should never get to this point if goes through int_float_converter first.
    return -1
# check if its an int for bounds
# l = 3
# print(type(l))
# if(type(l) == int):
# 	print("yes")

# def check_bounds():
#     if lower_bound < upper_bound:
#         if int(lower_bound) and int(upper_bound):
#             return True
#         if float(lower_bound) and float(upper_bound):
#             return True
#         else:
#             print("One of the bounds is not a number")  #Should never get to this point if goes through int_float_converter first.
#             return False
#     else:
#         print("The lower bound is not less that the upper bound")
#         return False


# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound

# m, b can be floats or integers
# the bounds must be integers, if not return false
y_list = math_man(12)
print(y_list)

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list



print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
a_input = 0
b_input = 0
c_input = 0


def quadratic_formula_calculator(x):
    a_input = input("please enter your 'a' value")
    b_input = input("please enter your 'a' value")
    c_input = input("please enter your 'a' value")