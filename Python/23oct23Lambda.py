#Lamba to find cube
inputData=int(input("Enter the input: "))
x= lambda x: x**3
print(x(inputData))

def binaryFun(x,y):
    return(x^y)
xVal=int(input("Enter the X input: "))
yVal=int(input("Enter the Y input: "))
print(binaryFun(xVal,yVal))
