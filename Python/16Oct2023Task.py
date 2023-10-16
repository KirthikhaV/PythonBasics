#Task 1: Write a program that calculates and displays the letter grade for a given
# numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59
a=float(input("Enter the score: "))
if 90<= a <=100:
    result="A"
elif 80<= a <=89:
    result = "B"
elif 70<= a <=79:
    result = "C"
elif 60<= a <=69:
    result = "D"
else:
    result = "F"
print(f"The grade for the marks {a} is {result}")

"""Task 2 : Leap Year Checker:
Create a program that determines whether a given year is a leap year.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
Input = 2024
Output = Leap year"""
def leap_year_check(y):
    if((y%4==0 and y%100!=0) or (y%400==0)):
        return "Leap year"
    else:
        return "Not a Leap year"
yearVal=int(input("Enter the year to check: "))
print(leap_year_check(yearVal))

"""Triangle Classifier:Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is 
equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input - side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3"""
def check_Triangle(side1,side2,side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif (side1 == side2 or side1 == side3 or side2 == side3):
        return "Isosceles"
    else:
        return "Scalene"

side1=int(input("Enter the value for side1: "))
side2=int(input("Enter the value for side2: "))
side3=int(input("Enter the value for side3: "))
print("The type of Triangle is :", check_Triangle(side1,side2,side3))
