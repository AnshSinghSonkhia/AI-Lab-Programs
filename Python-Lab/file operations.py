# Creating a file and writing to it
with open("demo_file.txt", "w") as file:
    file.write("Hello, this is a demo file.\n")
    file.write("We are learning file operations in Python.\n")

# Reading from the file
with open("demo_file.txt", "r") as file:
    content = file.read()
    print("Content of the file:")
    print(content)

# Appending to the file
with open("demo_file.txt", "a") as file:
    file.write("Appending some more text to the file.\n")

# Reading the file again to see the changes
with open("demo_file.txt", "r") as file:
    updated_content = file.read()
    print("\nUpdated content of the file:")
    print(updated_content)
