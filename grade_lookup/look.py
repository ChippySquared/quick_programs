# Problem: We are a teacher who needs a quick way to look up the grades of our
# students. We decide to use a hash table to store each student's name and
# their corresponding grade.

# Task
# To implement a system where you can:
# 1) Add student names and their grades to the hash table.
# 2) Look up a student's grade by their name.
# 3) Handle cases where a student's name does not exist in the table.

# Approach: a constant time O(1) search using a hash table is best for this as
# it only needs a key(a student name in this case) and a value (the student's
# grade).

# We add an example of grades.
grades = {}

grades["Jack"] = 7
grades["Olivia"] = 9
grades["Bert"] = 8
grades["Sarah"] = 6
grades["John"] = 5


# A hash table is a dictionary in Python. Function to retrieve grades.
def lookup_grade(student_name):
    if student_name in grades:
        return f"{student_name}'s grade is: {grades[student_name]}"
    else:
        return f"No grade found for {student_name}."


# We lookup for John's grade here as an example.
print(lookup_grade("John"))
