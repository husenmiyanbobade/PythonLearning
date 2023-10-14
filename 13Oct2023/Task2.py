#Write a Python program to calculate the area of a circle given its radius using the formula
#area=π×r^2 ( Take pie as 3.14)
pie = 3.14
radius= float(input("Enter the radius: "))
areaOfCircle = pie*(radius**2)
print("area of the circle is : ",areaOfCircle)

#Create a program that takes two numbers as input
#and prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2 :
    print(num1 ,"is greater than " ,num2)
elif num1 < num2 :
    print(num1 ,"is less than " ,num2)
else :
    print (num1 ,"is equal to " ,num2)