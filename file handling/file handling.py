# Read from a file
with open("read.txt", "r") as file:
    content = file.read()
    print(content)

# Write to a file
with open("sri.txt", "w") as file:
    file.write("This is a new line.")

# Append to a file
with open("sri.txt", "a") as file:
    file.write("\nThis line is appended.")

# Read the updated file
with open("sri.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)


with open("sri.txt", "r+") as file:
    content = file.read()
    print("Original Content:", content)


    file.write("Additional line.\n")
    file.seek(0)  # Move the file pointer to the beginning
    modified_content = file.read()
    print("Modified Content:", modified_content)


with open("sri.txt", "w+") as file:
    file.write("This is a new line.\n")
    file.seek(0)  # Move the file pointer to the beginning
    content = file.read()
    print("Content:", content)



