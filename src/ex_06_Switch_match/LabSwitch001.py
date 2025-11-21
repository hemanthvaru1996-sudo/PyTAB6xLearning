day=int(input("Enter the day\n"))
match day:
    case 1:
        print("The Day is Monday")
    case 2:
        print("The Day is Tuesday")
    case 3:
        print("The Day is Wednesday")
    case 4:
        print("The Day is Thursday")
    case 5:
        print("The Day is Friday")
    case 6:
        print("The Day is Saturday")
    case 7:
        print("The Day is Sunday")
    case _:
        print("The Day is Unknown")