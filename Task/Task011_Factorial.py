# 5! = 5*4*3*2*1 = 120
# 0! is always 1
# num=5
# num = int(input("Enter the number you want : "))
# fact=1
# if num<=0:
#     print("Factorial is" ,fact)
# else:
#     for i in range (1,num+1):
#         fact=fact*i
#     print("Factorial is",fact)
#         #print("num")
num=6
factorial=1

for i in range(1, 7):
    factorial = factorial * i
print(factorial)
print(f"Factorial of a number {num} is {factorial} ")

