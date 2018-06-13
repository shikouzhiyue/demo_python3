import os
def select_something(string_name, address='.'):
   for x in os.listdir(address):
       x = os.path.join(address, x)
       if os.path.isdir(x):
           select_something(string_name, x)
       elif string_name in x:
           print(x)

if __name__ == "__main__":
    string_name = input("Please input any key to find: ")
    address = input("Where to search: ")
    select_something(string_name, address)
