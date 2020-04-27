import random

students = ["Bobby", "Emma", "Lars", "Jack", "James"]

# Information about the list
print(len(students))
print(random.choice(students))
print(random.shuffle(students))

# Deleting something from the list
del students[2]
print(students)

# Changing a value from the list
students[4] = "Donald"
print(students)
