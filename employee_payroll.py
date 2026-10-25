class Employee:
    def __init__(self, employee_id, name, basic_salary, overtime_hours):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.overtime_hours = overtime_hours

    def calculate_gross_salary(self):
        return self.basic_salary + (self.overtime_hours * 500)

    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        return gross_salary - (gross_salary * 0.10)

    def calculate_tax(self):
        return self.calculate_gross_salary() * 0.10

employee1 = Employee("EMP101", "Alice", 50000, 10)
employee2 = Employee("EMP102", "Brian", 65000, 6)

employees = [employee1, employee2]

for employee in employees:
    print("Employee ID:", employee.employee_id)
    print("Name:", employee.name)
    print(f"Gross Salary: KSh {employee.calculate_gross_salary():,.2f}")
    print(f"Tax: KSh {employee.calculate_tax():,.2f}")
    print(f"Net Salary: KSh {employee.calculate_net_salary():,.2f}")
    print()
