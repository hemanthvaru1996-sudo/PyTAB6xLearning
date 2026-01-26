#1.Functions with NO parameter and NO return type
def greet():
    print("Hello")

greet()

#2 No return type but with Arg/Parameter.
def your_name(name):
    print("Hello",name)
your_name('Hemanth')

#3 No return type with Default Argument
def default_name(name="Vaun"):
    print("Hello",name)
    print("Hello", name.upper())
default_name(name="Vaun")
default_name(name="Kaavi")

#Multiple Arguments
def multiple_argument(a1='ravi' , a2='Usha'):
    print("Hey..!",a1,a2)
    print("Hey..!",a2.upper())
multiple_argument()
multiple_argument(a2="Kiran")
multiple_argument(a1='Girish',a2="Harish")

#4 Reurn type + Argument

def sum_of_two_numbers(number1, number2):
    return number1 + number2

result=sum_of_two_numbers(1,2)
print(result)
result=sum_of_two_numbers(100,102)
print(result)
print('----------------------------------------------------------------------')
def default_areguments_sum(n1=100,n2=200):
    print('The sum of Two Numbers')
    return n1*n2
r=default_areguments_sum(200,30)
print(r)
print('----------------------------------------------------------------------')
x=default_areguments_sum()
print(x)