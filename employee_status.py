"""
This program stores and displays employee information.
It also demonstrates converting a number to a string
so that it can be joined with another string.
"""

employee_name = "Alice"
employee_age = 30
employee_salary = 50000.00
employee_active = True

print(f"Employee Name: {employee_name}")
print(f"Employee Age: {employee_age}")
print(f"Employee Salary: KSh {employee_salary:.2f}")
print(f"Employee Active: {employee_active}")

print("Employee age is " + str(employee_age) + " years.")
