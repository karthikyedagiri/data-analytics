'''
SETS:
------->a set is a collection of unique and unordered elements.
----->duplicate values are not allowed.
----->items are not stored in index order.
---->{}
'''
any={1,2,2,3,4}
print(any)
'''
methods:
union():----it will give all the values or elements from 2 sets together in once.
syntax---->variable_name.union()
----
'''
any={1,2,2,3,5,7,8}
an={50,20,45}
print(any | an)
'''
intersection(): to get the common elements from both sides
syntax---->variable_name.intersection()
----------
'''
any={3,3,4,5,6}
an={3,67}
print(any & an)
print(any.intersection(an))
'''
difference():
----------->to get different values or elements from the set.
syntax--->variable_name.difference()
'''
any={3,3,4,5,6}
an={3,67}
print(any - an)
print(any.symmetric_difference(an))
