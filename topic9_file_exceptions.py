try:
    f = open("employees.txt", "r")
    contents = f.read()
    print(contents)
    f.close()
except FileNotFoundError:
    print("The employee file was not found.")
finally:
    print("File processing completed.")
