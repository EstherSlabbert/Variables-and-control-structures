 # Goal: Program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
 # included math extension to be able to use math functions for calculations
import math
print ("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print ("investment - to calculate the amount of interest you'll earn on your investment")
print ("bond - to calculate the amount you'll have to pay on a home loan")

 # User input to determine what to calculate
 # For investment: Total amount including simple interest OR total amount including compound interest.
 # Simple interest follows: A = P(1 + r * t).
 # Compound interest follows: A = P(1 + r) ^ t.
 # Where: ‘r’ is the percentage interest divided by 100. ‘P’ is the amount that the user deposits.‘t’ is the number of years that the money is being invested.‘A’ is the total amount once the interest has been applied.
 # For bond: Repayment due monthly.
 # Monthly bond repayment = (i.P)/(1 - (1+i)^(-n))
 # Where: ‘P’ is the present value of the house. ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12.‘n’ is the number of months over which the bond will be repaid.

print ("Please note that this initial input is not case sensitive.")
finance_type = input ("Please enter either 'investment' or 'bond': ")
finance_type = finance_type.lower ()
if finance_type != "investment" and finance_type != "bond":
    print ("Please restart and enter a valid entry.")
else:
    if finance_type == "investment":
        principal_amount = float (input ("Please enter the amount of money you are depositing: £"))
        interest_rate = float (input ("Please enter the percentage interest rate (please only enter numbers): "))
        years = float (input ("Please enter the number of years you plan on investing: "))
        interest = input ("\nNote that this entry is case sensitive.\nPlease enter 'simple' or 'compound' for your selected type of interest: ")

        if interest == "simple":
            total = principal_amount*(1 + (interest_rate/100)*years)
            total = round (total, 2)
            print (f"\nThe total amount you can expect for investing £{principal_amount} at a rate of {interest_rate}% for {years} years is £{total}.")

        elif interest == "compound":
            total = principal_amount*math.pow((1 + interest_rate/100), years)
            total = round (total, 2)
            print (f"\nThe total amount you can expect for investing £{principal_amount} at a rate of {interest_rate}% for {years} years is £{total}.")

        else:
            print ("Please restart and enter a valid entry.")
    elif finance_type == "bond":
        present_house_value = float (input ("Please enter your present house value: £"))

        print ("NOTE: If you only have the annual interest rate then you must divide that rate by 12 in order to get monthly interest rate.")
        interest_r8 = float (input ("Please enter the percentage monthly interest rate (numbers only): "))

        num_months = float (input ("Please enter the number of months you plan to take to repay the bond: "))

        monthly_repayment = (interest_r8/100*present_house_value)/(1 - (1 + interest_r8/100)**(-1 * num_months))
        monthly_repayment = round (monthly_repayment, 2)

        print (f"\nIf you take out a bond at a monthly interest rate of {interest_r8} for a house presently valued at {present_house_value} and plan to repay it in {num_months} you will have to repay £{monthly_repayment} every month.")