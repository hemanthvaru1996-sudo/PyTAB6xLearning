def outer_function():
    var1=30

    def inner_function1():
        var2=40
        print(var1)
        print(var2)

    def inner_function2():
        var3=50
        print(var1)
        print(var3)
    inner_function1()

outer_function()