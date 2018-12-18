# Outline
* Data Structures of Pandas: Series and DataFrame
* Data Creation
* Data Indexing and Slicing

# Data Structures

## Series
Series is a one-dimensional labeled array and the labels are referred to as the index. Series is quite similar to ndarray and can be passed on to most numpy functions. 
However, **the key difference is that it's labeled indexed**, and you can actually define your own labeled index, such as using letters instead of numbers, to index and access the data. (numpy ndarray is indexed by nonnegative integers). 
As a result, **operations between Series will automatically align the data based on label**. When you do slicing, the index is also sliced, and you can get and set values by index like you're dealing with a fixed-size dict.

## DataFrame
DataFrame is a 2-dimensional labeled data structure. Each column is a Series objects and you can think of the DataFrame as a dict
of Series objects. Here, index serves as row labels and column names serve as column labels. Like Series, operations between DataFrames will automatically
align the data based on labels, here both row labels and column labels.

# Data Creation

## Series
```
import numpy as np
import pandas as pd

s = pd.Series(data, index=index)
```
Here, data can be a python dict, an ndarray, or a scaler value; the index is a list of axis labels. If no index is passed, range(len(data)) will be
automatically used as index.
```
# from dict
d = {'p1':1, 'p2':2, 'p3':3, 'p4':4, 'p5':5}
s = pd.Series(d)
# from ndarray
s = pd.Series(np.random.randn(5), index = ['p1', 'p2', 'p3', 'p4', 'p5'])
# from scaler value
pd.Series(1.0, index = ['a', 'b', 'c'])
```
## DataFrame
```
df = pd.DataFrame(data, index=index, columns=columns)
```
Here, data can be a python dict, an ndarray, a Series, or another DataFrame.
```
# from dict
d = {'height': pd.Series([155, 160, 175, 180], index = ['p1', 'p2', 'p3', 'p4']),
     'weight': pd.Series([90, 120, 150], index = ['p1', 'p2', 'p3'])}
df = pd.DataFrame(d) # as mentioned above, match by row labels(index). Missing weight for p4 is filled with NaN automatically.
df = pd.DataFrame(d, index = ['p3','p2','p1']) # only keep records and order by index p3, p2, p1
df.index
df.columns

d = {'height': [155, 160, 175],
     'weight': [90, 120, 150]}
df = pd.DataFrame(d, index = ['p1','p2','p3'])

d = [{'height': 155, 'weight': 90}, {'height': 160, 'weight': 120}, {'height': 175, 'weight': 150}]

# from ndarray
d = np.array([[155, 90], [160,120], [175,150]])
df = pd.DataFrame(d, index = ['p1','p2','p3'], columns = ['height','weight'])
```

# Data Indexing and Slicing

## Series

Series is ndarray-like and dict-like, and the operations are similar to that of array or dict. 
```
# array-like
s[0]
s[:3]
s[::-1]
s[s > s.median()]
s[[1, 3, 5]]
np.exp(s)

# dict-like
s['a']
'a' in s
s.get('a', np.nan)
```

## DataFrame

Operation |	Syntax
--------- | --------- 
Select column | df[col] 
Select row by label	| df.loc[label] 
Select row by integer location |	df.iloc[loc] 
Slice rows |	df[5:10] 
Select rows by boolean vector | df[bool_vec]	
```
df['height']
df.loc['p1':'p2', :] == df.loc['p1':'p2'] # return all columns from row p1 to row p2
df.iloc[0, 1:2]
df[::2] 
df[df['height'] > 160]
```
