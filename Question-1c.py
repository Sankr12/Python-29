# Write a python script to print the following status of a file:
# c. which file opening mode is used

def opening_mode(filename,Mode):
    try:
        with open(filename, Mode) as file:
            print(f"file {filename} Open mode is {file.mode}")

    except FileNotFoundError:
        print("File Not Found")
    except Exception as e:
        print(f"An error occured {Exception}")

file = input("Enter file name: ")
Mode = input("Enter the mode[r/w/a/r+/w+/a+]: ")

opening_mode(file,Mode)