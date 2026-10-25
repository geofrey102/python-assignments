student_name = input("Enter student name: ")
examination_mark = int(input("Enter examination mark: "))

if examination_mark < 0 or examination_mark > 100:
    print("Invalid mark")
elif examination_mark >= 70:
    grade = "A"
elif examination_mark >= 60:
    grade = "B"
elif examination_mark >= 50:
    grade = "C"
elif examination_mark >= 40:
    grade = "D"
else:
    grade = "F"

if 0 <= examination_mark <= 100:
    print("\nSTUDENT RESULTS")
    print(f"Student Name: {student_name}")
    print(f"Examination Mark: {examination_mark}")
    print(f"Grade: {grade}")
