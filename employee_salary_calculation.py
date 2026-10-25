employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
monthly_deduction = float(input("Enter monthly deduction: "))

housing_allowance = 0.10 * basic_salary
gross_salary = basic_salary + housing_allowance
net_salary = gross_salary - monthly_deduction

print(f"Employee Name: {employee_name}")
print(f"Basic Salary: KSh {basic_salary:.2f}")
print(f"Housing Allowance: KSh {housing_allowance:.2f}")
print(f"Gross Salary: KSh {gross_salary:.2f}")
print(f"Monthly Deduction: KSh {monthly_deduction:.2f}")
print(f"Net Salary: KSh {net_salary:.2f}")
