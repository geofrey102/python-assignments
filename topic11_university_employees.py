class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def displayEmployee(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)

class Lecturer(Employee):
    def __init__(self, name, employee_id, teaching_subject):
        super().__init__(name, employee_id)
        self.teaching_subject = teaching_subject

    def displayLecturer(self):
        self.displayEmployee()
        print("Teaching Subject:", self.teaching_subject)

lecturer = Lecturer("Dr. Mary Mueni", "EMP001", "Python Programming")
lecturer.displayLecturer()
