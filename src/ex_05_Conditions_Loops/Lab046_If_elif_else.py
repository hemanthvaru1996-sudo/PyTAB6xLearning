# Problem  Find the Max between 3 numbers

# Logic Building

# User inputs - num1, num2, num3 -> int
# O/p -> int or String with max number .

num1=int(input("Enter the num1 \n "))
num2=int(input("Enter the num2 \n "))
num3=int(input("Enter the num3 \n "))

# 5 > 3 and 5 >2 ->  5
# num1 > num2 and num1 > num3 -> num1
# num2 > num1 nad num2 > num3 -> num2
# num3 - max

if num1 >= num2 and num1 >= num3:
    print("Max", num1)
elif num2 >= num3 and num2 >= num1:
    print("Max", num2)
else:
    print("Max", num3)
