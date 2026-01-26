import math
#
# num=int(input("Enter a number:"))
# op=lambda num : math.pow(num,2)
# res= op(num)
# print(res)

print(lambda: math.pow(int(input("Enter a number:")),2)())
