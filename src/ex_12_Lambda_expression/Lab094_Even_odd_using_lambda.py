user_input=int(input("Enter a number:"))

check_Even_odd= lambda num : 'even' if num%2==0 else 'odd'
print(check_Even_odd(user_input))
