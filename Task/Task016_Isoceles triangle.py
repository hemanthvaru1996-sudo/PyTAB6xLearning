# def triangle(side1,side2,side3):
#     if side1==side2==side3:
#         print('the triangle is equilateral Triangle')
#     elif side1==side2 or side2==side3 or side3==side1:
#         print('The triangle is isosceles Triangle')
#     else:
#         print('The triangle is scalance')
# triangle(3,3,3)
# triangle(2,3,2)
# triangle(1,2,3)


a= int(input("Enter the Side A\n"))
b= int(input("Enter the Side B\n"))
c= int(input("Enter the Side C\n"))

def classify_triangle(a,b,c):
    if a>0 and b>0 and c>0:
        if a==b==c:
            return 'Equilateral'
        elif a==b or a==c or b==c:
            return 'Iscoceles'
        else:
            return 'Scalene'
    else:
        return 'Invalid input'


result = classify_triangle(a,b,c)
print(f"the traingle is classified as : {result}")