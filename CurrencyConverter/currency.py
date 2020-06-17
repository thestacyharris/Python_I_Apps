# ===
# Program Name: harris-lab2-assign2.py
# Lab no: 2
# Description:  Temperature Conversion App
# Student:  Stacy Harris
# Date:  6/12/2020
# ===

from datetime import datetime
import math

title = "US Dollar Currency Converter"

print(title)

def main():
    try:
        usd_input = float(input("Enter the number of US Dollars you want to convert:"))
    except ValueError:
        print("Please enter only numbers.")
        print()
        main()

    usd = usd_input * 1
    formatted_usd = format(usd, '.2f')
    eur = 0.90231 * usd
    formatted_eur = format(eur, '.2f')
    gbp = 0.81752 * usd
    formatted_gbp = format(gbp, '.2f')
    inr = 71.7937 * usd
    formatted_inr = format(inr, '.2f')
    aud = 1.48338 * usd
    formatted_aud = format(aud, '.2f')

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y")

    print("{0} USD is equal to {1} EUR, {2} GBP, {3} INR, and {4} AUD as of".format(formatted_usd, formatted_eur, formatted_gbp,
                                                                               formatted_inr, formatted_aud)," as of: ",date_time,".\n")
    end()


# this function determines if user is finished with app and either exits or reruns the program
def end():
    end_result = input("Would you like to enter another conversion? Y or N ")
    if end_result.lower() == "n":
        print("Thank you for using this currency converter application.")
        exit()
    else:
        print()
        print("*" * 80)
        main()


main()


