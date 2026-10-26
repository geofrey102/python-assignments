employees = {
    "Alice": 50000,
    "Brian": 65000,
    "Catherine": 55000,
    "David": 60000,
    "Emily": 58000
}

for name, salary in employees.items():
    print(f"{name}: KSh {salary:,.2f}")

employees["Brian"] = 70000
employees["Francis"] = 52000

total_salary = sum(employees.values())

print("Updated Employee Records:", employees)
print(f"Total Salary Payable: KSh {total_salary:,.2f}")
