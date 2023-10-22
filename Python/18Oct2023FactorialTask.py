#Factorial series
def factorialFunc(num):
    if num<=0:
        result= "Invalid"
    else:
        result=1
        for i in range(1,num+1):
            result=result*i
    return result

inputNum=int(input("Enter the value to get factorial: "))
print(factorialFunc(inputNum))




