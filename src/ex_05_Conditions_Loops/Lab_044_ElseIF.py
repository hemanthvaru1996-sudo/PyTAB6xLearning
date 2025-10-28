"""
Find the given number is Even or ODD
How to find a even or odd number
Divide by 2: If the number can be divided by 2 with no remainder, it is an even number.
"""
num = int(input("Enter the Number:"))
# if num>=0:
#     if num % 2 == 0:
#          print("Even")
#     else:
#          print("Odd")
# else:
#     print("Negative number")
if num>=0:
    print("Even" if num % 2 == 0 else "Odd")

else:
    print("Negative number")