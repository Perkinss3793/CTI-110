# Learning to use dictionaries
# Each entry consists of a key:value pair

# Create a dictionary where the keys are student IDs and the values are names.
students = {"001":"Kevin", "002":"Suzie", "003":"Kate"}

# print(students)

# Give the key, have Python to return the value
print(students["002"])
print(students ["003"])
print(students ["001"])

# print(students["002"],)

# Get the student id from the user
student_id = input("Enter a student id: ")

# Using the student_id from the user, have Python return the value
print(students[student_id])


###############################################################################################
# Add a key:value pair into an existing dictionary
students["004"] = "Dion"

print(students)

# Delete a key:value pair from the dictionary
del students["001"]

print()
print()
print("Kevin Graduated, yay!")
print()
print(students)