numbers =[1,2,3,4,5]

def sq(num):
    return num ** 2

sq_of_all_numbers=list(map(sq,numbers))
print(sq_of_all_numbers)