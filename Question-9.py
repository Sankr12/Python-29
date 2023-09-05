# Write a python script to store book data in a file. Book data is
# in the form of a dictionary in which book name is the key and 
# price is its value. Use pickle to store data into a file (say bookfile)

import pickle

book = {'Maths':400, 'Physics':500, 'Chemistry':350, "Hindi":200, 'Physical Education':250}

f = open('Bookfile.pkl','ab')
pickle.dump(book,f)

f.close()

