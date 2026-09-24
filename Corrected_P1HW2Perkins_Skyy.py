# Skyy Perkins
# 9/13/2026
# Corrected - P1HW2 - 24Sep26
#This program calculates and displays travel expenses

# Get your budget amount
budget_amount = float(input("Enter your budget amount: "))

# Get your travel destination
travel_destination = input("Enter your travel destination: ")

# Get your gas expense
gas_expense = float(input("Enter the estimated amount of money that you will spend for gas: "))

# Get your accomodation expense
accomodation_expense = float(input("Enter the approximate amount that you will need for accomodation/hotel: "))

# Get your food expense
food_expense = float(input("Enter the amount that you will spend for food: "))

print("--------------Travel Expenses-------------")

#Display Travel Destination
print(f"Location: {travel_destination}")

#Display Initial Budget
print(f"Initial Budget: {budget_amount}")


#Display Fuel Expense
print(f"Gas Expense: {gas_expense}")

#Display Accomodation Expense
print(f"Accomodation Expense: {accomodation_expense}")

#Display Food Expense
print(f"Food Expense: {food_expense}")

# Add expenses
add_expenses = gas_expense + accomodation_expense + food_expense




#Display Remaining Balance
remaining_balance = budget_amount - gas_expense - accomodation_expense - food_expense
print("The remaining balance:", remaining_balance)