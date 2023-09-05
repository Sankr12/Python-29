# Write a python script to count the number of python keywords occuring in a a python source file

import keyword

python_keywords = keyword.kwlist

def count_keywords(filename):
    try:
        keywords_count = 0
        with open(filename, 'r') as file:
            for line in file.readlines():
                for item in python_keywords:
                    if item in line:
                        keywords_count += 1
        print(f"Number of Python keywords in '{filename}': {keywords_count}")
    except FileNotFoundError:
        print("File Not Found")

filename = input("Enter a Python file name: ")
count_keywords(filename)
