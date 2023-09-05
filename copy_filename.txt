# Write a python script to append list of city names in a file 'cities.txt'

cities = ["Chandigarh", "Kolkata", "Noida", "Nainital", "Pune"]

f = open('cities.txt','a+')

a=0
for city in cities:
    city = str(a)+". "+city
    f.write('\n'+city)
    a+=1