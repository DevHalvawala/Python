#Write a Python program to add an item in a tuple.
#20CS018-Dev Halvawala

tuple = (4, 6, 2, 8, 3, 1) 
print(tuple)

tuple = tuple + (9,)
print(tuple)

tuple = tuple[:5] + (15, 20, 25) + tuple[:5]
print(tuple)

list = list(tuple) 

list.append(30)
tuple = tuple(list)
print(tuple)
