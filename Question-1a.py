# write a python script to print the following status of a file
# a. Whether a file is read only

import os

def check_status(filename):
    if os.path.exists(filename):
        if os.access(filename,os.R_OK):
            print(f"{filename} is readable (not read-only)")
        else:
            print(f"{filename} is read-only")
    else:
        print(f"{filename} not exist")

filename = input("Enter an existing file: ")
check_status(filename)