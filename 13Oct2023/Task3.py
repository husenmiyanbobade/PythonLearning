#Use the ternary operator to find the maximum of three numbers entered by the user.

num1 =int(input("Enter number 1:\n"))
num2 =int(input("Enter number 2:\n"))
num3 =int(input("Enter number 3:\n"))

maxnumber= (num1 if (num1>num2 and num1>num3) else num2 if(num2>num1 and num2>num3) else num3 )
print("max number is : ",maxnumber)

# Develop a Python script that calculates the square and cube of a given number.

num4 = int(input("enter the number :\n"))
print("square of input number is ",num4**2)
print("cube of input number is ",num4**3)