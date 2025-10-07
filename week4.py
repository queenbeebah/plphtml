# File Read & Write Challenge + Error Handling Lab

# Ask the user for the input filename
filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Modify the file content (example: convert to uppercase)
    modified_content = content.upper()

    # Write the modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"File has been successfully read and modified content written to '{new_filename}'.")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except IOError:
    print("Error: The file cannot be read or written.")
