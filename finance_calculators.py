# importing math to use in the formula on line 21
import math

print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print() # printing a blank line
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# asking the user for their choice and converting this to lowercase to allow all capitalisations of the word
option = input("Enter your choice").lower()

# if the input from the user isn't equal to "bond" and isn't equal to "investment", this message is displayed and the program stops
if (option != "bond") and (option != "investment"):  
    print("Please select an option") 

if option == "investment":
    deposit = float(input("How much money are you depositing?"))
    investment_interest_rate = float(input("What is the interest rate? Only enter a number."))
    num_of_years = float(input("How many years do you plan on investing?"))
    interest = input("Do you want 'simple' or 'compound' interest?")
    if interest == "simple":
        total_simple_interest = deposit * (1 + (investment_interest_rate / 100) * num_of_years) # calculating the simple interest
        rounded_total_simple_interest = round(total_simple_interest, 2) # rounding to 2 decimal places as this is currency
        print("Your total simple interest is £" + str(rounded_total_simple_interest)) # this will display the total simple interest
    elif interest == "compound":
        total_compound_interest = deposit * math.pow((1 + (investment_interest_rate / 100)), num_of_years) # calculating the compound interest
        rounded_total_compound_interest = round(total_compound_interest, 2) # rounding to 2 decimal places as this is currency
        print("Your total compound interest is £" + str(rounded_total_compound_interest)) # this will display the total compound interest

if option == "bond":
    house_value = float(input("Enter the value of the house."))
    bond_interest_rate = float(input("Enter the interest rate."))
    bond_annual_interest_rate = bond_interest_rate / 100 # calculating the annual interest rate as a decimal to use in the formula on line 30
    num_of_months = float(input("Enter the number of months you plan to take to repay the bond."))
    repayment = ((bond_annual_interest_rate / 12) * house_value) / (1 - (1 + (bond_annual_interest_rate / 12)) ** (-num_of_months)) # calculating the monthly bond repayments
    rounded_repayment = round(repayment, 2) # rounding to 2 decimal places as this is currency
    print("Your monthly repayment is £" + str(rounded_repayment)) # this will display the total monthly repayments on the bond