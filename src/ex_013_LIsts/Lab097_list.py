my_list=[1,2,3]
my_list[0]='Pramod'
#print(my_list)
my_list[1]='dutta'
#print(my_list)
for items in my_list:
    print(items)

print("------------------------------------------------------------")

my_list1=[1,2,3]
print("Element at the index 0 is ",my_list1[0])
print("Element at the index 1 is ",my_list1[1])
print("Element at the index 2 is ",my_list1[2])
print("------------------------------------------------------------")
my_list1.append(4)
print(my_list1)

my_list1.append(5)
print(my_list1)
print("------------------------------------------------------------")
my_list1.extend([6,7,8,9,10])
print(my_list1)

print("------------------------------------------------------------")
my_list1.insert(1,'Hemanth')
print(my_list1)
print(len(my_list1))
print("------------------------------------------------------------")
# my_list1.remove('Hemanth')
# print(my_list1)
print("------------------------------------------------------------")
my_copy_list=my_list1.copy()
print(my_list1)
print(my_list1.copy())

my_copy_list.remove('Hemanth')
# print(my_list1)
print(my_list1.copy())