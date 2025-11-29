"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
    1.   Opens and reads a text file named sample.txt.
    2.   Prints its content line by line.
    3.   Handles errors gracefully if the file does not exist.
"""

try:
    FILE = "sample.txt"
    line_num = 1
    with open(FILE, "r") as file:
        file_content = file.readlines()
        # content = [x.strip() for x in file_content if x.strip()] # First x => Output if condition True, Second x => Get one by one value from list, Third x => Check condition, No need use 'strip' while print data because here we use in first x
        content = list(filter(lambda c: c.strip() != "", file_content))
        if len(content) == 0:
            print("Empty File...")
        else:
            print("Reading file content...")
            for line in content:
                print(f"Line {line_num}: " + line.strip())
                line_num = line_num + 1
except FileNotFoundError:
    print(f"Error: The file '{FILE}' was not found.")
except Exception as ex:
    print(f"Error: {ex}")

# ------------------------------------------------------------------------------------------------------
print("\n")

"""
Task 2: Write and Append Data to a File
Problem Statement: Write a Python program that:
    1.   Takes user input and writes it to a file named output.txt.
    2.   Appends additional data to the same file.
    3.   Reads and displays the final content of the file.
"""

try:
    FILE = "output.txt"
    write_content = input("Enter text to write to the file: ")
    with open(FILE, "w") as file:
        file.write(write_content + "\n")
    print(f"Data successfully written to '{FILE}'.\n")

    append_content = input("Enter additional text to append: ")
    with open(FILE, "a") as file:
        file.write(append_content + "\n")
    print("Data successfully appended.\n")

    with open(FILE, "r") as file:
        file_content = file.read()
    print(f"File content of '{FILE}':\n{file_content}")
except Exception as ex:
    print(f"Error: {ex}")
