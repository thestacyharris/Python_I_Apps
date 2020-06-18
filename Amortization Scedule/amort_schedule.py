# ===
# Program Name: harris-lab3-assign2.py
# Lab no: 3
# Description:  Simple Python command line loan amortization app
# Student:  Stacy Harris
# Date:  6/18/2020
# ===

from prettytable import PrettyTable
import datetime
from dateutil.relativedelta import  *

def banner():
    print("*************************************")
    print("**                                 **")
    print("**  Loan Amortization ScheduleApp  **")
    print("**                                 **")
    print("*************************************\n")


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

    start_date = input('Enter the start date of the loan in YYYY-MM-DD format')
    year, month, day = map(int, start_date.split('-'))
    date1 = datetime.date(year, month, day)

    mortgageCalcuation(date1, loan_amt, years, interest_rate)

    end()


# this function take the input values from main() and calculates the monthly payment for the mortgage
def mortgageCalcuation(date1, loan_amt, years, interest_rate):
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

    end_result = input("Would you like to see the amortization table of the loan? Y or N ")
    if end_result.lower() == "y":
        amort_schedule(date1, loan_amt, months, monthly_apr, monthly_payment)

    else:
        end()


# this function creates a table showing the amortization schedule of the loan
def amort_schedule(date1, loan_amt, months, monthly_apr, monthly_payment):

    # variables for the table
    payment_no = 1
    balance = loan_amt
    interest_paid = monthly_apr * balance
    total_interest = interest_paid
    principal_paid = monthly_payment - interest_paid
    balance = balance - principal_paid

    # code of the PrettyTable amortization schedule
    amort_table = PrettyTable(['Payment Date', 'Payment', 'Principal', 'Interest', 'Total Interest',  'Balance'])
    while payment_no <= months:
        amort_table.add_row([f"{date1: %b %Y}", f"${monthly_payment:,.2f}", f"${principal_paid:,.2f}",
                             f"${interest_paid:,.2f}", f"#{total_interest:,.2f}",  f"{balance:,.2f}"])
        payment_no += 1
        date1 = date1 + relativedelta(months=+1)
        interest_paid = monthly_apr * balance
        total_interest = interest_paid + total_interest
        principal_paid = monthly_payment - interest_paid
        balance = balance - principal_paid

    print(amort_table)


# this function determines if user is finished with app and either exits or reruns the program
def end():
    end_result = input("Would you like to enter another loan amount? Y or N ")
    if end_result.lower() == "n":
        print("\nThank you for using this mortgage payment calculator.")
        exit()
    else:
        print()
        print("*" * 80)
        print()
        main()


main()
