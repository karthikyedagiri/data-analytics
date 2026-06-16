'''
                                                                Data Analysis
                                                                ---------------
---> This is process of inspecting, cleaning,transfroming and modeling data to discover useful insights...
Types  of DA
--------------
1)Descriptive Analysis ---> summarizing Data
2)Diagnostic Analysis ---> Understanding causes
3)Predective Analysis ---> Forecasting future outcomes
4)Prescriptive Analysis ---> Suggesting acting based on data

Why DA
-------
---> To improve decision making
---> Detects trends & patterns

                                                                    Numpy
                                                                    ------
--->This python library for numerical computing, it provides support for multi-dimensional arrays,
    and linear algebra operations, making it essential for data analysis...

using numpy in DA
------------------
---> Improved performance
---> Simplifies complex operations
---> Easy data manipulation...
Ex:-
'''
import numpy as np
arr_1 = np.array([1,2,3,4])
print(arr_1)
                                                                    
import numpy as np
arr_1 = np.array([[4,5,6,7],[1,2,3,4]])
print(arr_1)

import numpy as np
arr_1 = np.array([[4,5,6,7],[1,2,3,4]])
print(arr_1.shape)           

import numpy as np
arr_1 = np.array([[5,6,7],[1,2,3]])
print(arr_1.shape)           
reshaped = arr_1.reshape(3,2)
print(reshaped)

import numpy as np
arr_1 = np.array([10,20,30,40,50])
print(arr_1[2])
print(arr_1 + 5)

import numpy as np
arr_1 = np.array([[1,2],[4,5]])
arr_2 = np.array([[5,6],[7,8]])
print(np.dot(arr_1, arr_2))

import numpy as np
arr_1 = np.array([10,20,30])
nrm_copy = arr_1.view()
arr_1[0] = 100
print(nrm_copy)
print(arr_1)

copy_dee = arr_1.copy()
arr_1[1] = 200
print(copy_dee)
print(arr_1)

'''
                                                                Pandas
                                                                -------
---> The pandas is a powerful data manipulation and analysis library..
---> where it provides data structure like series and dataframe for efficiency data handling...
Ex:-
'''
import pandas as pd
any = pd.Series([2999,15999,25999,4999,1999], index = ['Earbuds','Smartphone','Laptop','Watch','Adapter'])
print(any)

'''
Method Series
--------------
1)Mean()
2)Sum()
3)Max()
4)Min()
5)Apply()
6)Map()

Dataframe
----------
'''
import pandas as pd
data = {'Product':['Earbuds','Smartphone','Laptop','Watch','Adapter'], 'Brand':['pro-2','Oneplus','ASUS','Bolt','oneplus'],
        'Price': [1599,50000,53999,1999,3999]}
dip = pd.DataFrame(data)
print(dip)


























