'''
conditoion statements:
----------------------
if-----> to check whether the statement true or not

num=5
if num%2==0:
    print("even")
else    :
    print("odd")

if-else:----> else in the if statement, incase the condition becomes false then it will enter into flow-back(else),
it will execute what ever inside it.

num=int(input("enter the number:"))
if num%2!=0:
    print(f"{num} is a odd number")
else:
    print(f"{num} is a even number")


age_=int(input(" enter ur age:"))
if age_>=18:
    print("we are eligible")
else:
    print(f"we have to wait {18-age} years")
'

year=int(input("enter the year:"))
if (year % 4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is a not leap year")
'''
num=9
if num>=0:
    print(f"{num} is a positive number")
else:

    print(f"{num} is negative number")
    
