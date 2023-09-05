# Write a python script to print the following status of a file:
# d. Name of the file

def filename(filename):
    try:
        with open(filename,'r') as file:
            print(f"Name of file: {file.name}")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occured {e}")

file = input("Enter existing file: ")
filename(file)