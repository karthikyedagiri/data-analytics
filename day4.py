'''
concatination:
------------> the + symbol for an int and can add,but for the other data types it will act as concatinating in the data type

a=90
b=8
print(a+b)
any_="python"
so="is a language"
print(any_ + so)
an=[1,2]
am=[3,4]
print(an+am)

tuple:
----->collection of diffenrt data types seperated by commas,represented in () and immutable.
some=(1,"python",[1,2],(3,4))
print(some.index(1))

Methods
------
count()
--->this is used to count the particular item in the tuple
syntax--->variable_name.count(item)

some=(1,"python",[1,2],(3,4))
print(some.count(1))

index()
------> used to find out the index position of the item, and only gives the first occurance.
any=[3,4,"python",[7,8]]
print(any[2][3])


some=(1,[1,2],(3,4),"python")
print(some.index("python"))

Dictionary:
--------
------> dict is a key: value pair,key and value is seperated by: and pair is seperated by comma
------->represented by ()

karthi={"name":"karthi",
               1:2,
               (1,2):[3,4]}
print(karthi)               

methods
------
keys():
----> usd to get all the keys
syntax: dict.key()

karthi={"name":"karthi",
               "age":45,
    
             (1,2):[3,4]}
print(karthi.keys())

values()
------> used to get all values from the dict
syntax: dict.values()

karthi={"name":"karthi",
               "age":45,
    
             (1,2):[3,4]}
print(karthi.values())

items()
------>used to get ke and value together.
syntax: dict.items()

karthi={"name":"karthi",
               "age":45,
    
             (1,2):[3,4]}
print(karthi.items())

karthi={"name":"karthi",
               "age":45,
    
             (1,2):[3,4]}
print(karthi.keys())

karthi={"name":"karthi",
               "age":45,
    
             (1,2):[3,4]}
print(karthi.items())


update()
------->used to add a new key:value pair into dict
syntax: dict.update({key:value})

clear()
------>used to remove all the items in the dict
'''
karthi={"name":"karthi",
               "age":45,
    
             (1,2):[3,4]}
karthi.clear()
print(karthi)
















































