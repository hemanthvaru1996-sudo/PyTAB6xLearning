def add_security(func):

    def wrapper():
        print("1.Before Function is called")
        print("2.Add helmet , Knee guards,License")
        func()
        print("3.After Function is called")
        print("Safe driving, leave all the other itmes")
    return wrapper()


@add_security
def driving_ola_scooter():
    print("i am Driving Ola Scooter")