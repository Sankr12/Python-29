# Write a python script to store a list of city names in a file 'cities.txt'

i = int(input("Enter how many cities you want to enter: "))

f = open('cities.txt','w')

for a in range(i):
    city = input(f"{a+1}. city name: ")
    cities = str(a+1)+'. '+city
    f.write(cities+'\n')

f.close()