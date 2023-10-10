class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Alex", "A001", 3.8),
        Student("Bunny", "B002", 3.5),
        Student("Chirs", "C003", 3.9),
        Student("Dav", "D004", 3.7)
    ]

    # Print the original student list
    print("Original student list:")
    for student in students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

    # Sort the students based on CGPA
    sorted_students = sort_students(students)

    # Print the sorted student list
    print("\nSorted student list based on CGPA:")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
