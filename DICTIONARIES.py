# NAME- DHRUVI VAISHNAV 
# ID NO- 20CE156

                                               # DICTIONARIES


 #   a. Write a Python script to check whether a given key already exists in a dictionary.


students = {'Dhruvi' :156,
'khushi': 151,
'Riyaa': 30,
'Krishna' : 20,
'payal' : 77
}
def key_in_dict(d, key) :
  return (key in d) 

print(key_in_dict(students, 'khushi'))
print(key_in_dict(students, 'hima'))


     


# b. Write a Python script to merge two Python dictionaries.

dic1 = {
    'a':'1',
    'b':'2',
}

dic2 = {
    'c':'3',
    'd':'4',
}
print(dic1.update(dic2))
print(dic1)



# c. Write a Python program to sum all the items in a dictionary.

dic = {
    'a': 1,
    'b':6,
    'c':3,
    'd':4,
}
print(sum(dic.values()))



# d. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dic = {

   0:10,
   1:20,
}
print(dic)
dic.update({2:30})
print(dic)



# e. Write a Python script to concatenate following 
# dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={
    1:10, 
    2:20
    }

dic2={
    3:30, 
    4:40
    }

dic3={
    5:50,
    6:60
    }
    
dic4={}  

dic1.update(dic2)
dic1.update(dic3)
dic4.update(dic1)
print(dic4)
