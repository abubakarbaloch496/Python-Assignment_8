# Displays student marks and finds the top scorer
# Create a dictionary of students and their marks
students = {
    "Ali": 80,
    "Sara": 90,
    "Ahmed": 75
}

# Print all student names
print("Student Names:")
for name in students.keys():
    print(name)

# Print all marks
print("\nStudent Marks:")
for marks in students.values():
    print(marks)

# Find the highest marks
highest_marks = max(students.values())

# Find the student with highest marks
for name, marks in students.items():
    if marks == highest_marks:
        print("\nTop Student: " + name + " with " + str(marks) + " marks")