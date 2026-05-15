'''
time_=input("Enter 24 hours time:")
parts_=time_.split(":")
hour_=int(parts_[0])
min_=int(parts_[1])
print(f"(time_)is converted into {hour_ - 12}:{min_} pm")

List:
-----
----> list is a collection of differnt data type and it is represented [] and seperated by ,
---->it is a mutable
methods
---->
append()
------
----> this method is used to add new item into list,and it will in the last index position
syntax
----->variable.name.append(item)
extend()---->this method is used to add itterable into list,and it will in the last index position,each value or substring is each index in the list.
--->syntax---> variable_name.extend(itterable)

pop()
----
---->it is used to remove the item from the list,but will mention here index position in the pop method

syntax---> variable_name.pop(index position)

remove()
---->it is used to remove the item from the list,but will mention here direct in the remove method

syntax
---->variable_name.remove()


b=[1,"python",[1,2]]
print(b)

a=[1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],34,[3,4]]
print(a[2][4])

a=[3,5,8]
a.append(10)
print(a)

immutable-->could not able to modify on that particular variable eg: int,str
mutable--->it can able to modify on that particular variable

hi="python is a"
print(hi.replace("python","ai"))
print(hi)
bye=[3,5,6]
print(bye.append(50))
print(bye)

heloo=[4,5,7]
heloo.pop(2)
print(heloo)
'''
so=["python",90,"java"]
so.remove("python")
print(so)






























