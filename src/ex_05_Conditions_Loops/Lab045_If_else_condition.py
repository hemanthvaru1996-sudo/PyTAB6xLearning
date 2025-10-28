# WAP to find out maximum number
#
# logic building
# 1. I/P :- interger or float
# 2.O/P :- integer or float

num1= float(input("Enter the num1 "))
num2=float(input("Enter the num2 "))
# if num1 > 0 and num2>0:
#     print("Positive Number")

# if num1 > num2:
#     print("Maximum",num1)
# else:
#     print("minimum",num2)

print("Maximum" if num1>num2 else "minimum")