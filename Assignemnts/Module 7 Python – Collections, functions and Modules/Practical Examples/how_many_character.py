#Write a Python program to count the number of occurrences of each character in a given string and print the results.

input_string = "hello world"  
char_count = {}  
for char in input_string: 
    if char in char_count:  
        char_count[char] += 1  
    else:
        char_count[char] = 1  
print("Character counts:", char_count)  

for char,count in char_count.items():
    print(f"'{char}': {count}")
