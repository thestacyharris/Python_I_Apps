# ===
# Program Name: harris-lab1-assign1.py
# Lab no: 1
# Description:  Simple Python command line calculator app
# Student:  Stacy Harris
# Date:  6/4/2020
# ===

title = "Simple Python Calculator"

print(title)

def main():
    try:
        global num1
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("Please enter only numbers.")
        print()
        main()

    try:
        global num2
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter only numbers.")
        print()
        main()

    global operator
    operator = input("Enter the operation: (+, -, *, /) ")

    if (operator == "/") and (num2 == 0):
        print("Error!! Cannot divide by zero!")
        print()
        main()

    # This converts the variables the from float to int if no decimal is present
    if num1 % 1 == 0:
        num1 = int(num1)
    if num2 % 1 == 0:
        num2 = int(num2)

    calc()

# this function does the calculation of the input values
def calc():
    if operator == "+":
        total = num1 + num2
        if total % 1 == 0:
            total = int(total)
        print(title, "\n")
        print("The sum of {0} and {1} is {2}, where addition is the operation entered"
              ", {0} and {1} are the numbers entered, and {2} is the product of the operation".format(num1, num2, total))

    elif operator == "-":
        total = num1 - num2
        if total % 1 == 0:
            total = int(total)
        print(title, "\n")
        print("The difference of {0} and {1} is {2}, where subtraction is the operation entered"
              ", {0} and {1} are the numbers entered, and {2} is the product of the operation".format(num1, num2, total))

    if operator == "*":
        total = num1 * num2
        if total % 1 == 0:
            total = int(total)
        print(title, "\n")
        print("The product of {0} and {1} is {2}, where multiplication is the operation entered"
              ", {0} and {1} are the numbers entered, and {2} is the product of the operation".format(num1, num2, total))

    if operator == "/":
        total = num1 / num2
        if total % 1 == 0:
            total = int(total)
        print(title, "\n")
        print("The quotient of {0} and {1} is {2}, where division is the operation entered"
              ", {0} and {1} are the numbers entered, and {2} is the product of the operation".format(num1, num2, total))
    end()


def end():
    end_result = input("Would you like to do another calculation? Y or N ")
    if end_result == "N" or "n":
        exit("Thank you for using the calculator")
    else:
        print()
        print("-" * 80)
        main()

main()


