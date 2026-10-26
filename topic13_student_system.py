class Student:
    def __init__(self):
        self.name = ""
        self.registration_number = ""
        self.course = ""
        self.mark = 0.0

    def setStudentDetails(self, name, registration_number, course, mark):
        self.name = name
        self.registration_number = registration_number
        self.course = course
        self.mark = mark

    def calculateGrade(self):
        if self.mark >= 70:
            return "A"
        elif self.mark >= 60:
            return "B"
        elif self.mark >= 50:
            return "C"
        elif self.mark >= 40:
            return "D"
        else:
            return "F"

    def displayStudentDetails(self):
        print("Student Name:", self.name)
        print("Registration Number:", self.registration_number)
        print("Course:", self.course)
        print("Mark:", self.mark)
        print("Grade:", self.calculateGrade())
        print()

def displayStudents(student_list):
    for student in student_list:
        student.displayStudentDetails()

students = []

for number in range(1, 4):
    print(f"Enter details for student {number}")
    name = input("Student name: ")
    registration_number = input("Registration number: ")
    course = input("Course: ")

    while True:
        try:
            mark = float(input("Mark: "))
            break
        except ValueError:
            print("Invalid mark. Please enter a number.")

    student = Student()
    student.setStudentDetails(name, registration_number, course, mark)
    students.append(student)

displayStudents(students)

f = open("students.txt", "w")

for student in students:
    print(f"Student Name: {student.name}", file=f)
    print(f"Registration Number: {student.registration_number}", file=f)
    print(f"Course: {student.course}", file=f)
    print(f"Mark: {student.mark}", file=f)
    print(f"Grade: {student.calculateGrade()}", file=f)
    print(file=f)

f.close()

print("Student details and grades saved to students.txt.")
