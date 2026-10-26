class Student:
    def __init__(self):
        self.name = ""
        self.registration_number = ""
        self.course = ""
        self.mark = 0

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

student = Student()
student.setStudentDetails("Alice Wanjiku", "UNI001", "Computer Science", 85)
student.calculateGrade()
student.displayStudentDetails()
