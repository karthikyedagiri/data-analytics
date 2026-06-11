'''
FILE HANDLING:
-------------
---------->>>>file handler is an object of file to maintain several function of file like,creating,reading,updating and deleting the file.

open a file:
-------
1.open()
2.with open()


modes:
-----
--->>
  'r'-->>is used to reading the file,error if file doesnot exist..
  'a'-->>is used to add the text into file,if file doesnot exist..
not exist...
'w'-->>is used to add the text into file but it will override of all text inside file.if the file does not exist it will create with that name.
'x'-->>used to create the file.
'r'-->>mode to create.

method:
------
write()
read()
---->>this method can read entire file chunk by chunk where we can specify the side.
readline()
readlines()

any_=open('karthi.txt','r')
print(any_.read())
any_.close()
'''
any_=open('karthi.txt','r')
print(any_.readlines())
any_.close()
