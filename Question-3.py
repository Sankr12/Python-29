# Write a python script to read the previously created file 'myfile.txt'
# and display content on the console.

with open('myfile.txt','r') as f:
    print(f.read())