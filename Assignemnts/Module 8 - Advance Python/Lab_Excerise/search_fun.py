import re

mystr = "Hello My name is danish and I am learning python"

x = re.search("danish",mystr)

print(x)

if x:
    print("Sucesss!")
else:
    print("Error!")