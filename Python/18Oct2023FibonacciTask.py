#Fibonacci series
def fibonacciFunc(num):
    if num<=0:
        print("Invalid")
    elif num ==1:
        print("0 1")
    else:
        a=0
        b=1
        print(a, end=" ")
        print(b, end=" ")
        for i in range(2,num):
            c=a+b
            print(c, end=" ")
            a,b=b,c
fibonacciFunc(int(input("Enter the value to get Fibonacci series: ")))



