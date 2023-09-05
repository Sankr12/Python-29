# Write a python script to extract book data from a bookfile using pickle.
# Also print extracted book data

import pickle

f = open('Bookfile.pkl','rb')
s = pickle.load(f)

for key in s:
    print(f"Book: {key} --> Price: {s[key]}")

f.close()