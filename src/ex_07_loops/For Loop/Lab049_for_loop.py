# for i in range(0,10,1):
#     print(i)
#
# # if i want to increase 2 step
#
# for i in range (0,10,2):
#     print(i)
class Dog:
    # A
    name = None
    breed = None
    height = None
    weight = None
    def __init__(self):
        print("I will be called")

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass


# Object Ref
chow_ref = Dog()
mow_ref = Dog()

