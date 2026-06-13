import re
name=input("Enter the name:")
c=re.fullmatch(r'^[A-Za-z]{3,}$',name)
if c:
    print("name is valid")
else:
    print("name is invalid")
mobile=input("Enter the number:")

a=re.fullmatch('[6-9][0-9]{9}',mobile)
if a:
    print("This is valid")
else:
    print("This is invalid")
password=input("Enter the password:")

b=re.fullmatch('[a-zA-Z0-20][0-9][!@#$%^&*]{8,16}',password)
if b:
    print("The password is valid")
else:
    print("The password is invalid")

