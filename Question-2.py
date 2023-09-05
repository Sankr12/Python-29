# Write a python script to create a new file 'myfile.txt' and store user entered text.

def store_data(filename,text):
    with open(filename,'w') as f:
        f.write(text)

filename = input("Enter the file name: ")
text = input("Enter the text you want to input into the file")

store_data(filename,text)