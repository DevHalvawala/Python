#Write a Python script to check whether a given key already exists in a dictionary.
dict={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def does_key_exist(x):
    if x in dict: 
        print("Key exist!")
    else:
        print("Key does not exist!")
does_key_exist(3)
does_key_exist(7)

# 20CS018-Dev Halvawala