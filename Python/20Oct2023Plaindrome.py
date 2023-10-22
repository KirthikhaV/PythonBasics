#palindromeFunc Task
def palindromeFunc(a):
    inpreverse=a[::-1]
    if a==inpreverse:
        return ("Palindrome")
    else:
        return ("Not a Palindrome")

inputData=input("Enter the input: ")
print(palindromeFunc(inputData))




