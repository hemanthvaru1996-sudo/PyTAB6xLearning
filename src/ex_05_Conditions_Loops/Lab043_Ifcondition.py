"""
take use age as input and print if he can go to goa or not
Step 1 :-
i/p -> Integer -> age
o/p -> string -> he gan go to club or not
step 2 Rough Logic:-
age >21 -> He can go to club
age <21 -> he can't go to club
"""
#Step 3:- Logic

age=int(input("Enter the age :\n"))
if age >=21:
    print("He can go to club")
else:
    print("He can not go to club")