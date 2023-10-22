#SumOfDigits Task
def SumOfDigit(a):
    sum=0
    while a>0:
       sum=sum+(a%10)
       a=a//10
    return (sum)
def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))
inputNum=int(input("Enter the input: "))
#print(SumOfDigit(inputNum))
print(sumDigits(inputNum))




