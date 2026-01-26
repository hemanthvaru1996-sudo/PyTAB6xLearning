num1 = int(input("Enter a number first Number:\n "))
num2 = int(input("Enter a number Second Number:\n "))
num3 = int(input('Enter a number Third Number: \n'))

def sum_of_three(n1=100,n2=200,n3=300):
    return n1+n2+n3
result = sum_of_three(num1,num2,num3)
print(result)
print('_________________________________________________________________')
result1 = sum_of_three()
print(result1)
print('_________________________________________________________________')
result2=sum_of_three(30,40,50)
print(result2)
print('_________________________________________________________________')
result3=sum_of_three(n1=11)
print(result3)
