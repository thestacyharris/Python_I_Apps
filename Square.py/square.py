# ===
# Program Name: harris-lab1-assign2.py
# Lab no: 1
# Description:  Simple Python command line square root calculator app
# Student:  Stacy Harris
# Date:  6/4/2020
# ===

import math

title = "Simple Square Root Calculator"
print(title)
print("-" * 29)

# this is the main function.  it receives the input variables from the user.
# it asks the user for a number to square root.
def main():
    try:
        global num1
        num1 = float(input("What number would you like the square root of? "))
    except ValueError:
        print("Please enter only numbers.")
        print()
        main()

    # This converts the variables the from float to int if no decimal is present
    if num1 % 1 == 0:
        num1 = int(num1)


    # This determines is the input number is positive or negative and runs the
    # appropriate function.
    if num1 < 0:
        negative_square()
    else:
        square_root()

# this block calculates the square root of real numbers
def square_root():
    # This converts the square root result from float to int if no decimal is present
    square_result = float(math.sqrt(num1))
    if square_result % 1 == 0:
        square_result = int(square_result)

    print("The square root of {0} is {1}.".format(num1, square_result))

    end()

# this block handles negative numbers.  it converts the negative number to positive
# so that the program can conduct the calculation.  the output adds the letter "i"
# to the result to indicate an imaginary number.
def negative_square():
    num1_positive = abs(num1)

    # This converts the square root result from float to int if no decimal is present
    square_result = float(math.sqrt(num1_positive))
    if square_result % 1 == 0:
        square_result = int(square_result)

    print("The square root of {0} is {1}i.".format(num1, square_result))

    end()

# this function determines if user is finished with app and either exits or reruns the program
def end():
    end_result = input("Would you like to do another calculation? Y or N ")
    if end_result.lower() == "n":
        exit("Thank you for using the calculator")
    else:
        print()
        print("*" * 80)
        main()

main()
