# This code demonstrates the use of try-except-finally blocks in Python to handle exceptions when working with files. The finally block ensures that resources are cleaned up properly, even if an error occurs.

try:
    file = open("output.txt", "r")  
    data = file.read()
    print("File content:")
    print(data)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

finally:
    
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so nothing to close.")