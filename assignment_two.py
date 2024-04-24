#Empty list
my_list = []

#Elements to be appended in the list
elements = [10,20,30,40]
for i in elements:
    my_list.append(i)
print(my_list)


#Insert the value 15 at the second position in the list
my_list.insert(2,15)
print(my_list)

#Extend my_list with another list
new_list = [50,60,70]

my_list.extend(new_list)
print(my_list)

#Remove the last element from
del my_list[-1]
print(my_list)


#Sort my_list in ascending order

my_list.sort()
print(my_list)

#Find and print the index of the value 30

index = my_list.index(30)
print(index)
