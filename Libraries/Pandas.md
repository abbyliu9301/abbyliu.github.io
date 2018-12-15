# Data Structures

## Series
Series is a one-dimensional labeled array and the labels are referred to as the index. Series is quite similar to ndarray and can be
passed on to most numpy functions. 
However, **the key difference is that it's labeled indexed**, and you can actually define your own labeled index, such as using letters instead of numbers, to index and access the data. (numpy ndarray is indexed by nonnegative integers). 
As a result, operations between Series will automatically align the data based on label. When you do slicing, the index is also sliced, and you can get 
and set values by index like you're dealing with a fixed-size dict.

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

# from ndarray

```
