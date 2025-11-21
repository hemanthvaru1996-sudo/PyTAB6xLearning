print("Enter the wich test you want to run")
test_type = input("Enter the Test Type: API , UI , Performance , Security \n")
match test_type:
    case 'API':
        print("We are running Postman API testcases")
    case "UI":
        print("We are running Selenium UI testcases")
    case "Performance":
        print("We are running Performance testcases")
    case "Security":
        print("We are running Security testcases")
    case _:
        print("Invalid.")

# Using if -else
#
# print("Enter which test you want to run")
# test_type = input("Enter the Test Type: API , UI , Performance , Security \n")
#
# if test_type == "API":
#     print("We are running Postman API testcases")
# elif test_type == "UI":
#     print("We are running Selenium UI testcases")
# elif test_type == "Performance":
#     print("We are running Performance testcases")
# elif test_type == "Security":
#     print("We are running Security testcases")
# else:
#     print("Invalid.")