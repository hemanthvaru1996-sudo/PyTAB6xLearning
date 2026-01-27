shopping_list_wife=('bread','Butter','Panner')
#shopping_list_wife[2]="milk" # TypeError: 'tuple' object does not support item assignment
print(shopping_list_wife)


# Real usage of tuple
my_tuple=("tta.com","sdet.com",'w3c.com')
my_api_list = list(my_tuple)
print(my_api_list)

my_api_list=tuple(my_tuple)
print(my_api_list)

hero1=("Batman","Bruce wayne")
hero2=("Wonder woman","diana prince")
new_tuple=(hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[0][0])
print(new_tuple[0][1])
print(new_tuple[1][1])
