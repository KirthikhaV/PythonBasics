#Count vowels and consonants in a String
def vowelFunc(a):
    vowCount =0
    consCount = 0
    vowList=['a','e','i','o','u']
    for i in a:
        if i in vowList:
            vowCount+=1
        else:
            consCount+=1
    if vowCount>0:
        return (f"In {a} there are {vowCount} vowels and {consCount} consonants.")
    else:
        return (f"No vowels found.Only {consCount} consonants are there in {a}.")
inputData=input("Enter the input: ")
print(vowelFunc(inputData.lower()))