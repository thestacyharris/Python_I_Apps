# ===
# Program Name: harris-lab2-assign1.py
# Lab no: 2
# Description:  Temperature Conversion App
# Student:  Stacy Harris
# Date:  6/12/2020
# ===

import os.path

title = "Temperature Conversion Application"

print(title)


def main():
    print("Would you like to convert from Fahrenheit to Centigrade or Centigrade to Fahrenheit?")
    convert_input = input("For from Fahrenheit to Centigrade enter: F \n For Centigrade to Fahrenheit enter: C\n")
    convert_input = convert_input.capitalize()

    if convert_input == "F":
        far_to_cent()
    elif convert_input == "C":
        cent_to_far()
    else:
        print("Please enter F or C")
        main()


def far_to_cent():
    fahrenheit_temp = float(input("Enter you temperature you would like to convert: "))
    centigrade_temp = (5 / 9) * (fahrenheit_temp - 32)
    centigrade_temp = float(round(centigrade_temp, 2))
    print("{0} Fahrenheit is equal to {1} Centigrade.".format(fahrenheit_temp, centigrade_temp))
    write_to_file(fahrenheit_temp, centigrade_temp)
    end()


def cent_to_far():
    centigrade_temp = float(input("Enter you temperature you would like to convert: "))
    fahrenheit_temp = (((9 / 5) * centigrade_temp) + 32)
    fahrenheit_temp = float(round(fahrenheit_temp, 2))
    print("{0} Centigrade is equal to {1} Fahrenheit.".format(centigrade_temp, fahrenheit_temp))
    write_to_file(fahrenheit_temp, centigrade_temp)
    end()


def write_to_file(fahrenheit_temp, centigrade_temp):
    if os.path.exists('temp_conversion.txt'):
        with open("temp_conversion.txt", "a") as conversions:
            conversions.write("  {0}\t\t\t\t\t   {1}\n".format(centigrade_temp, fahrenheit_temp))
    else:
        with open("temp_conversion.txt", "a") as conversions:
            conversions.write("Centigrade\t\t\t\tFahrenheit\n")
            conversions.write("__________\t\t\t\t__________\n")
            conversions.write("  {0}\t\t\t\t\t   {1}\n".format(centigrade_temp, fahrenheit_temp))


def end():
    end_result = input("Are you sure you wish to exit? Y or N ")
    if end_result.lower() == "y":
        exit()
    else:
        print()
        print("*" * 80)
        main()


main()
