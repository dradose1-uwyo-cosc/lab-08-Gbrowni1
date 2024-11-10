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

if type(int_float_converter(rando_string))==int or type(int_float_converter(rando_string))==float:
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
# check if its an int for bounds
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def pointslope_y_calculator():
    """Calculates 'y' output and generates a list for x values of given bounds"""
    while True:
        m = input("Please enter value for m:")
        if m.upper() == "EXIT":
            print("Function terminated")
            break
        
        b = input("Please enter value for b:")
        if b.upper() == "EXIT":
            print("Function terminated")
            break
        
        lower_bound = input("Please enter value for lower bound:")
        if lower_bound.upper() == "EXIT":
            print("Function terminated")
            break
        
        upper_bound = input("Please enter value for upper bound:")
        if upper_bound.upper() == "EXIT":
            print("Function terminated")
            break
        
        y_list = []
        m_val = int_float_converter(m)
        b_val = int_float_converter(b)
        lower_bound_val = int_float_converter(lower_bound)
        upper_bound_val = int_float_converter(upper_bound)

        if lower_bound_val > upper_bound_val:
            print("Lower bound should not be greater than upper bound.")
            continue

        if type(lower_bound_val) != int:
            print("Lower bound is not an integer.")
            return False
        if type(upper_bound_val) != int:
            print("Upper bound is not an integer.")
            return False
        
        for x in range(lower_bound_val, upper_bound_val + 1):  # inclusive upper bound
            y = m_val * x + b_val
            y_list.append(y)
            print(f"For x = {x}, y = {y}") 
        print(f" y-list is: {y_list}")

    return
pointslope_y_calculator()
    
print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quadratic_formula_calculator():
    """Takes user input, verifies proper input, and sends to quadratic_computation function to compute"""

    while True:
        a_input = input("Please enter value for a:")
        b_input = input("Please enter value for b:")
        c_input = input("Please enter value for c:")

        a = int_float_converter(a_input)
        b = int_float_converter(b_input)
        c = int_float_converter(c_input)

        def quadratic_computation():
            x_1 = (-b+((b^2)-4*a*c)^(1/2))/2*a #plus
            x_2 = (-b-((b^2)-4*a*c)^(1/2))/2*a #minus
            return x_1, x_2
