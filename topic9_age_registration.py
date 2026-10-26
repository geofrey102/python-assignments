age_input = input("Enter your age: ")

try:
    age = int(age_input)
    print("Age successfully recorded")
except ValueError:
    print("Invalid age entered")
