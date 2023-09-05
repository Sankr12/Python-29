# write a python script to print the following status of a file
# b. whether a file is closed or not

def check_status(filename):
    f = None
    try:
        f = open(filename,'r')
        print(f"file {filename} is opened now")

        if f.closed:
            print(f"file {filename} is closed")
        else:
            print(f"file {filename} is not closed")
    
    except FileNotFoundError:
        print(f"{filename} not exist")
    except Exception as e:
        print(f"An error occured {e}")
    finally:
        if f is not None and not f.closed:
            f.close()
            print(f.closed)

file = input("Enter a file: ")
check_status(file)