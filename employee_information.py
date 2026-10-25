employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
employee_age = int(input("Enter employee age: "))
basic_salary = float(input("Enter basic salary: "))

annual_salary = basic_salary * 12

print(f"Employee Name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"Employee Age: {employee_age}")
print(f"Basic Salary: KSh {basic_salary:.2f}")
print(f"Annual Salary: KSh {annual_salary:.2f}")
