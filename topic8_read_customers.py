f = open("customers.txt", "r")

contents = f.read()
print(contents)

f.close()

print("r: Opens a file for reading.")
print("w: Opens a file for writing and erases existing contents.")
print("a: Opens a file for adding new content without deleting existing content.")
