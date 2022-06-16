#Write a Python script to merge two Python dictionaries.
dict_1={'x':9, 'y':10, 'z':11}
dict_2={'p':12, 'q':13, 'r':14}

dict_3=dict_2.copy()
dict_3.update(dict_1)

print (dict_3)
# 20CS018-Dev Halvawala