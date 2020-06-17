# ===
# Program Name: harris-lab3-assign1.py
# Lab no: 3
# Description:  Simple Python command line mortgage calculator app
# Student:  Stacy Harris
# Date:  6/16/2020
# ===


def banner():
    print("*******************************")
    print("**                           **")
    print("**  Mortgage Calculator App  **")
    print("**                           **")
    print("*******************************\n")


def main():
    banner()

    while True:
        try:
            loan_amt = int(input("Enter the amount of the loan:"))
            break
        except ValueError:
            print("Please enter only numbers.")
    while True:
        try:
            years = int(input("Enter the number of years: "))
            break
        except ValueError:
            print("Please enter only numbers.")
    while True:
        try:
            interest_rate = float(input("Enter the interest rate: "))
            break
        except ValueError:
            print("Please enter only numbers.")

    mortgageCalcuation(loan_amt, years, interest_rate)

    end()


# this function take the input values from main() and calculates the monthly payment for the mortgage
def mortgageCalcuation(loan_amt, years, interest_rate):
    months = years * 12
    monthly_apr = ((interest_rate / 12) / 100)
    
    # monthly payment formula is payment = loan amount times (c(1+c) to power of n) over (c(1+c) to power of n) minus 1
    # c = monthly interest rate, n = months of the loan
    
    # this calculates the numerator part of formula
    principal_numerator = ((1 + monthly_apr)**months) * monthly_apr
    # this calculates the denominator part of the formula
    principal_denominator = ((1 + monthly_apr)**months) - 1
    monthly_payment = loan_amt * (principal_numerator / principal_denominator)

    print("-" * 20)
    print(f"Loan amount: \t\t${loan_amt:,}")
    print(f"Number of years: \t{years}")
    print(f"Interest Rate:\t\t{interest_rate:.2f}%")
    print(f"Monthly Payment: \t${monthly_payment:,.2f}")


# this function determines if user is finished with app and either exits or reruns the program
def end():
    end_result = input("Would you like to enter another loan amount? Y or N ")
    if end_result.lower() == "n":
        print("\nThank you for using this mortgage payment calculator.")
        exit()
    else:
        print()
        print("*" * 80)
        main()


main()
