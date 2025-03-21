#created a list
my_list =[10,20,30,40]
print("Before Append" ,my_list)

my_list.append(20)

print("After Append",my_list)
#added my_list2 so that I can use the append method.
my_list2 = [50,60,70,80]
print(my_list2)

my_list.extend(my_list2)
print("List after append",my_list)

#removing the last element from my_list2
my_list2.remove(80)
print(my_list2)