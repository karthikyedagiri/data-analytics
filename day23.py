'''
                                                        REGULAR EXPRESSION(RegEx)
                                                       --------------------------
------------>>RegEx is a sequence of char that form a searching pattern..
------------>>this can be  used to check if a string contain the specified search pattern..

------>>python has a built-in package called 're' which can be Regular Expression(RegEx) 
--> RegEx is a sequence of char that form a searching pattern...
--> This can be used to check if a string contain a specific search pattern
--> python has a  built in package called 're' which can be used to work with RegEx...
[] --> a-z,A-z,0-9 and any specified sequence...
. --> Here each dot is one char
^ --> This looks for the , string is starting with specified sequence or not
Functions in re
----------
1. Fimdall
2. Search
3. full match

Metachar:
--------
[]--->> a-z,A-Z,0-9 and any specified sequence.
.--->> here each dot is one char.
^--->>this look for the,string is starting with specified sequence or not.
$--->>ending
*--->>zero or more
?--->>zero or one
+--->> one or more
{}-->>

Special sequence:
----------------
\S-->no space
\s-->only space
\D-->non-digit
\d-->only digits
\w-->matches any word char(letters,digits,underscore)
\W-->non words

import re
any_ = "C is a foundational, general-purpose programming language created by Dennis Ritchie at Bell Labs in 1972. Known for its high performance and low-level memory access, it is widely used to develop operating systems (like Linux and Windows kernels), embedded systems, and database"
print(re.findall('^java is',any_))

import re
any_="python is language"
print(re.findall('p.{9}',any_))

import re
any_="python is 420 language"
print(re.findall('\W',any_))

'''
import re
mobile=input("enter mobile number:")
how=re.fullmatch('[6-9][0-9]{9}',mobile)
who=re.fullmatch('[3-5][0-6]{5}',mobile)
a=re.fullmatch('[1-2][0-5][4]',mobile)
if how:
    print(f"{mobile} this is india number")
elif who:
     print(f"{mobile} this is russia number")
elif a:
    print(f"{mobile} this is china number")
else:
    print(f"{mobile} this is not india number")








