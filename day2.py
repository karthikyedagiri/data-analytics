'''

operators
1.arithmetic operators
-----+,-,%,/,//

print(2*3)
print(4%5==0)
print(10**2)
print(10/2)
print(35.24//5)

2.assignment operators
-----=,+=,-=,%=
count = 0
for j in range(1,10):
     count += 1
     print(count)
3.comparision operators
----
== >----looks for both values equal or not
 ,!=,>=,<=,>,<
4.logical operators
5.membership operators
6.identity operators
7.bitwise operators
count = 0
for j in range(1,10):
     count += 1
     print(count)

6.identity operators
---
is>--this operator looks for the object is same or not
is not


a = [1,2]
b = [1,2]
c = a
print(a==b)
print(id(a))
print(id(b))
print(a is c)
print(a is not c)

4.logical operator:
----and --> this is used to check both should be true.

a=15
if a%3==0 and a%5==0:
    print("true")

----or--->
a=5
if a%3==0 or a%5==0 :
    print("true")

5. membership:
------
in ,not in

a=7
b=[1,2,7,8]
print(a in b)

a=7
b=[1,2,7,8]
print(a not in b)

7.bitwise operators:
-------
&,|,<<,>>

print(5|3)

print(5&3)

print(5<<3)

print(5>>3)

STRINGS

---->strings is sequence of char that are enclosed in '',"",''''''' and string is immutable.

methods
-------
replace()--->used to replace with new substring
syntax---->variable_name.replace("old string","new string")

any="python is a language"
print(any.replace("python","java"))

any="python is a language"
print(any.replace("python","java"))
print(any)

split()--->it is used to seperate the parts and it  will split based on the substring where
 before substring is one index and after is another index in the list.
 syntax--->variable_name.split("substring")
 
any="python is a language"
print(any.split())

len()
------> get the number of items , substrings
syntax-->len(variable_name)

any="python is a language"
print(len(any))

slicing()---->
------>it can give the access to get particular index from the string.
syntax---> variable_name[starting index:ending index]

any="python is a language"
print(any[3:11])

Indexing
--------> used to get the substring present in that index position.
syntax---> variable_name[index position]
"substr".join(vari)
'''
any="python is a language"
print(any[7])
print(any.index("ang"))
                                   
