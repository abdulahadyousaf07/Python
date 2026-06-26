import os

# Specify the directory path
directory = input("Enter directory path: ")

try:
    # List all files and folders
    contents = os.listdir(directory)

    print("\nContents of the directory:")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("Permission denied.")