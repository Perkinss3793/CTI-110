# Skyy Perkins
# 09/22/2026
# P2HW2
# Write a program that asks the user to enter test grades for Modules 1 - 6 and performing computational functions.

# Get six test grades for module 1 - module 6 from user
Module1 = float(input("Enter the test grade for Module 1: "))
Module2 = float(input("Enter the test grade for Module 2: "))
Module3 = float(input("Enter the test grade for Module 3: "))
Module4 = float(input("Enter the test grade for Module 4: "))
Module5 = float(input("Enter the test grade for Module 5: "))
Module6 = float(input("Enter the test grade for Module 6: "))

# Store grades in a list
test_grades = [Module1, Module2, Module3, Module4, Module5, Module6]

print("-----------Results----------------------")

# Display the lowest test grade
print(f"Your lowest grade is {min (test_grades)}")

# Display the highest grade
print(f"Your highest grade is {max (test_grades)}")

# Add all of test grades to get the sum
sum_total = sum(test_grades)

# Display the sum of all test grades
print(f"The sum of test grades is {sum_total: .2f}")

# Get the average of items in the list

# Display the average of items in the list
print("Average:")

# Average of test grades
average = float(sum (test_grades) / len (test_grades))

print("-----------------------------------------------")