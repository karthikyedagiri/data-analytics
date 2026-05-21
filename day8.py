'''
'
marks=int(input("enter the marks:"))
if marks>=90:
    print("A+")
elif marks>=70:
    print("B+")
elif marks>=60:
    print("c")
elif marks>=50:
    print("pass")
elif marks>=30:
    print("fail")

''
''
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
if a>b and a>c:
      print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
''
nested if ---->
--------->if inside if
''
SBI_bank={"ATM PIN":"2817"}
pin=input("enter the 4 digit pin:")
if len(str(pin))==4:
    if pin in SBI_bank['ATM PIN']:
        print("welcome to SBI bank")
    else:
        print("INVALID")
else:
        print("pls enter the pin:")
''
for loop
--------
-----> used to itterate over a sequence.
''
any="python"
an=[4,5,6,7]
a=(7,8,9,0)
for i in any:
    print(i)
    ''
range()
------->range is a inbuilt function used to generate numbers in squence manner 
syntax--->range(start,end,step)
'
if i in range(2005,2026,3):
    print(i)

'
break
-----
----> used to exit from the loop based on the condition

continue
-------
------> used to skip the current itteration
''
for i in range(1,10):
    if i==3:
        print(i)

pass
----

''

for i in range(1,10):
    if i==3:
        pass

while
---it is the combination of for+if
'''
i=1
while i<5:
    print(i)
    i+=1





















