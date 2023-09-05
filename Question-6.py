# Write a python script to search whether a particular city is there in 
# the file cities.txt' or not 

def search(filename,city):
    try:
        with open(filename,'r') as file:
            for line in file.readlines():
                if city in line:
                    print(f"File has {city} city")
                    return
            else:
                print(f"File don't have {city} city")
    except FileNotFoundError:
        print("File Not Found")

city = input("Enter the city: ")
filename = 'cities.txt'
search(filename,city)