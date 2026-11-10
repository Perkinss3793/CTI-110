# Skyy Perkins
# November 10, 2026
# P5LAB
# Use loops, functions, and module imports to complete assignments

import random

def disperse_change(change):
    
    if change == 0:
        print("No change due")
        
    # Calculate the amount of each coin needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)
    
    num_quarters = change // 25
    change = change - (num_quarters * 25)
    
    num_dimes = change // 10
    change = change - (num_dimes * 10)
    
    num_nickels = change // 5
    change = change - (num_nickels * 5)
    
    num_pennies = change // 1
    
    # Display coins owed
    
    if num_dollars > 0:
        print(num_dollars, end='')
        if num_dollars == 1:
            print(" Dollar")
        else:
            print(" Dollars")
            
    if num_quarters > 0:
        print(num_quarters, end='')
        if num_quarters == 1:
            print(" Quarters")
        else:
            print(" Quarters")
            
    if num_dimes > 0:
        print(num_dimes, end='')
        if num_dimes == 1:
            print(" Dimes")
        else:
            print(" Dimes")
            
    if num_nickels > 0:
        print(num_nickels, end='')
        if num_nickels == 1:
            print(" Nickels")
        else:
            print(" Nickels")
            
    if num_pennies > 0:
        print(num_pennies, end='')
        if num_pennies == 1:
            print(" Pennies")
        else:
            print(" Pennies")
            
def main():
    
    # Generate a random float with 2 decimal places as the amount that the customer owes
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    
    # Display the amount owed
    print(f"You owe ${amount_owed:.2f}")
    
    # Prompt user to enter a float as the cash they will put into the checkout machine  
    amount = float(input("Enter the amount of money as a float: "))
    
    # Calculate the amount of change owed to the customer
    change_owed = amount - amount_owed    
    
    # Display change owed
    print(f"Change is: ${change_owed:.2f}")
    
    # Convert change owed to an integer
    change_owed = round(change_owed * 100)
    
    # Call the function and pass change_owed as the parameter
    disperse_change(change_owed)
    
# Call main function
main()