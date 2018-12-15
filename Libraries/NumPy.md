Numpy is a core library for scientific computing in Python. A numpy array is a grid of values of the same type.

## Create Arrays
```
import numpy as np
# all 0
a = np.zeros((1, 2))
# all 1
b = np.ones((2, 2))
# all 5
c = np.full((2, 2), 5)
# identity matrix
d = np.eye(3)
# random values
e = np.random.random((2,2))
# choose your own 
f = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# get dimensions of array: (3, 4)
print(f.shape)
```
Basically, numpy can take in tuples specifying shape and create numpy arrays. You can also specify all elements of the array.

## Indexing and Slicing
```
# first row
row0_f = f[0, :]
row0_f = f[0:1, :]
```
The difference lies in the shape of the returned results. Using slicing yields an array of the same rank (1,4) as the original array,
while integer indexing yields a lower rank (4,) in this case.
```
# second col
col1_f = f[:, 1]
col1_f = f[:, 1:2]
```
Similarly, interger indexing yields a shape of (3,) while slicing yields a shape of (3,1).
```
# get arbitrary positions
f[[0, 1, 2], [2, 1, 0]] == np.array([f[0, 2], f[1, 1], f[2, 0]])
```
The left hand specifies each position we want to access by specifying row index and column index separately and return a result array.
The right hand first get elements of each position, then turn the list of elements into a numpy array.

## Get Elements from Each Row
```
# create an array of column indices
col_idx = np.array([1, 2, 3])
# get element from each row: [2, 7, 12]
f[np.arange(3), col_idx] 
```

## Boolean Indexing
```
# get a numpy array of True/False of the same shape as f
bool_idx = (f > 6)
f[bool_idx] == f[f > 6]
```

## Math
```
x = np.array([[1,2],[3,4]], dtype = np.float64)
y = np.array([[5,6],[7,8]], dtype = np.float64)
```
### Elementwise operations
x + y, x - y, x * y, x / y, etc.
### Matrix multiplication
np.dot(x, y)
### Matrix transpose
x.T
### Sum and Cumulative Sum
```
np.sum(x)
# sum by row: [4, 6]
np.sum(x, axis=0)
# sum by col: [3, 7]
np.sum(x, axis=1)
# cumulative sum by row: [[1,2], [4,6]]
np.cumsum(x, axis = 0)
# cumulative sum by col: [[1,3], [3,7]]
np.cumsum(x, axis = 1)
```

## Broadcasting
```
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b = np.array([0,1,2])
# we can add b to each row of a by broadcasting
c = a + b
```
