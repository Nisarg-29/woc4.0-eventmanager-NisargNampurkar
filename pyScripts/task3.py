#task3
import re
from collections import defaultdict

#Python dictionary initialised for Contact keeper data
Directory=defaultdict(list)
print("Welcome to myContactKeeper.\n Choose 1 to add contact.\nChoose 2 to retrieve.\nChoose 3 to display all contacts.\nChoose any key other than above to quit.\n")
while 1:
    o=int(input("Choose any option\n"))
    if o==1:
        name=input("Name:")
        number=input("Number")
        Directory[name].append(number)
    elif o==2:
        subs=input("Write any word to search")
        res = [i for i in Directory.keys() if subs in i]
        print ("All names with given string as substring are : " + str(res))
        name=input("Write name of the person to retrieve contact")
        print(Directory[name])
    elif o==3:
        print(Directory)
    else:
        break
