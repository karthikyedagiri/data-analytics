'''
for i in range(1,10):
    for j in   range(1,2):
        print(j)

num=8
for i in range(1,21):
    print(f"{8}x{i}={i*num}")
    
so=input("enter the name:")
empty_str=""
for j in so:
    empty_str=j+empty_str
    print(empty_str)
if empty_str==so:
    print(f"{so} is palindrome")
else:
    print(f"{so} is not palindrome")


amstro_
''
num=int(input("enter the number:"))
amstro_=0
length_=len(str(num))
for i in str(num):
     amstro_ += int(i) ** length_
if amstro_==num:
        print(f"{num} is amstrong number")
else:
    print(f"{num} is not amstrong number")
        
''
perfect mbers:

''
num=int(input("enter the number:"))
per_nu=0
for j in range(1,num):
    if num%j==0:
        per_nu +=j
if per_nu==num:
    print(f"{num} is perfect num")
else:
    print(f"{num} is not perfect num")


''
hii=int(input("enter the number:"))
count=0
for i in range(1,num+1):
    if  hii%i==0:
        count +=1
if count ==2:
    print(f"{hii} is a prime number")
else:
    print(f"{hii} is not prime number")
''

for i in range(1,100,2):
    print(i)
    
star:
''
star=26
for i in range(1,star+1):
    for d in range(1,i+1):
        print(chr(64+d),end= " ")
    print()

star=24
for i in range(1,star+1):
    for d in range(1,i+1):
        print("*",end= " ")
    print()

star=24
count=0
for i in range(star,0,-1):
    for d in range(i):
        count+=1
        print("*",end=" ")
    print()

'''
hii=20
for i in range(1,hii+1):
    print(" "*(hii-i),end="")
    for j in range(1,i+1):
        print("*",end= " ")
    print()    


hii=26
for i in range(1,hii+1):
    print(" "*(hii-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end= " ")
    print()    



hii=26
count=int(input("enter the number:"))
for i in range(1,hii+1):
    print(" "*(hii-i),end="")
    for j in range(1,i+1):
        print(count,end= " ")
    print()    



















        




















        
