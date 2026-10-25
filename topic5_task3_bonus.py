employee_name = input("Enter employee name: ")
years_of_service = int(input("Enter years of service: "))
performance_rating = int(input("Enter performance rating: "))

qualifies_for_bonus = years_of_service >= 3 and performance_rating >= 4

if qualifies_for_bonus:
    eligibility_result = "Employee qualifies for a bonus"
else:
    eligibility_result = "Employee does not qualify for a bonus"

print("\nEMPLOYEE DETAILS")
print(f"Employee Name: {employee_name}")
print(f"Years of Service: {years_of_service}")
print(f"Performance Rating: {performance_rating}")
print(f"Eligibility Result: {eligibility_result}")
