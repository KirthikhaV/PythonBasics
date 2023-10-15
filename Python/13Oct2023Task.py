#Task 2.1 - Calculate the area of the circle with radius
def calculate_circlearea(radius):
    # Using π as 3.14 i.e., area = 3.14 * r^2
    area = 3.14 * (radius ** 2)
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate_circlearea(radius)
print(f"The area of the circle with radius {radius} is: {area}")

#Task 2.2 - Create a program that takes two numbers as input and prints whether the first number
# is greater than, less than, or equal to the second number.
num1=int(input("Enter the First number: "))
num2=int(input("Enter the Second number: "))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1<num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

#Task 2.3 - Use the ternary operator to find the maximum of three numbers entered by the user.
num1=int(input("Enter the First number: "))
num2=int(input("Enter the Second number: "))
num3=int(input("Enter the Third number: "))
result=num1 if (num1>num2 and num1>num3) else (num2 if(num2>num3) else num3)
print(f"Max value out of {num1}, {num2}, {num3} is {result}")

#Task 2.4 - Develop a Python script that calculates the square and cube of a given number.
def calculate_power(inputVal, powerVal):
    return inputVal ** powerVal

inputNum=int(input("Enter the number to calculate its square and cube: "))
print(f"Square of given number is : ",calculate_power(inputNum,2))
print(f"Cube of given number is : ",calculate_power(inputNum,3))
