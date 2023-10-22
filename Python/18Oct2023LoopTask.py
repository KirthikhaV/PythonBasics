#Loop Task
def loopFunc(a,b):
    for i in range(1,b):
        if i==a:
            break
        else:
            print(i, end=" ")

inputNum=int(input("Enter the number to exit: "))
inputRange=int(input("Enter the range: "))
loopFunc(inputNum,inputRange)




