# Write a python script to create a copy of a file

def copy_file(filename):
    with open(filename,'r') as file:
        text = file.read()
    f = open('copied_file.txt','w')
    f.write(text)
    f.close()

select = input("Enter an existing file: ")
copy_file(select)