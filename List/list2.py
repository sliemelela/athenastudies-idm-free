students = ["Bobby", "Emma", "Lars", "Jack", "James"]
numbers = [2, 5, 9, -1.74, 7, 4, 2, 6]

# Finding the index
print(students.index("Lars"))

# Adding values to the list
students.append("Donald")
print(students)

# Adding values in a specific place in the list
students.insert(1, "Donald")
print(students)

# Sorting numbers
numbers.sort()
print(numbers)

# Sorting alphabetically
students.sort()
print(students)

# Sorting in reverse alphabetical order
students.sort(reverse=True)
print(students)

# Reversing the already existing list
students.reverse()
print(students)
