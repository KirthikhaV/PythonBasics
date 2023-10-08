# Get input from the user
n = int(input("Enter a number: "))

# Print the table using an f-string
print(f"{n} x 1 = {n * 1}")
print(f"{n} x 2 = {n * 2}")
print(f"{n} x 3 = {n * 3}")
print(f"{n} x 4 = {n * 4}")
print(f"{n} x 5 = {n * 5}")
print(f"{n} x 6 = {n * 6}")
print(f"{n} x 7 = {n * 7}")
print(f"{n} x 8 = {n * 8}")
print(f"{n} x 9 = {n * 9}")
print(f"{n} x 10 = {n * 10}")

#print the table using for loop
print("\nPrint the table using for loop")
for x in range(1,11):
    print(f"{n} x {x} = {n * x}")



#Task 3
"""
+------------------+-------------------------------------------------------------+
| Function         | Description                                                 |
+------------------+-------------------------------------------------------------+
| `len()`          | Returns the length of the string.                            
| `capitalize()`   | Converts the first character of the string to uppercase.     
| `lower()`        | Converts all characters in the string to lowercase.          
| `upper()`        | Converts all characters in the string to uppercase.          
| `title()`        | Converts the first character of each word to uppercase.      
| `count(sub)`     | Returns the number of occurrences of a substring in the      
|                  | string.                                                     
| `find(sub)`      | Returns the lowest index of the first occurrence of a        
|                  | substring. Returns -1 if the substring is not found.         
| `replace(old, new)` | Replaces occurrences of a substring with another substring. 
| `split(sep)`     | Splits the string into a list of substrings based on the     
|                  | specified separator.                                        
| `strip()`        | Removes leading and trailing whitespaces from the string.    

"""