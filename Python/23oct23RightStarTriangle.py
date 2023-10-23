#Right Triangle Star pattern Task
#*
#**
#***
#****
#*****
def starTriangleFunc(a):
    for i in range(0,a+1):
        for j in range(0,i):
            print("*", end=" ")
        print("\n")
inputData=int(input("Enter the input for number of stars: "))
starTriangleFunc(inputData)