# Skyy Perkins
# 09/29/2026
# P3HW1
# Use P2HW2 that covered Python lists that will display the accurage letter grade beased on the student's numeric grade average

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
avg = float(sum (test_grades) / len (test_grades))

print("-----------------------------------------------")

#Round average to the nearest integer
avg = round(avg)

# Branching to determine letter grade based on the average
if avg >= 90:
    grade_report = "A"
elif avg >= 80:
    grade_report = "B"
elif avg >= 70:
    grade_report = "C"
elif avg >= 60:
    grade_report = "D"
else:
    grade_report = "F" 
    
print()
print(f"Your average is {avg} so your final grade is {grade_report}")    