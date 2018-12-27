## Problem

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

## Example

Input:\
[\
 [ 1, 2, 3 ],\
 [ 4, 5, 6 ],\
 [ 7, 8, 9 ]\
]\
Output: [1,2,3,6,9,8,7,4,5]


Input:\
[\
  [1, 2, 3, 4],\
  [5, 6, 7, 8],\
  [9,10,11,12]\
]\
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

## Solution
Use dx, dy to indicate the direction of each step.
<img width="942" alt="screen shot 2018-11-16 at 8 35 11 pm" src="https://user-images.githubusercontent.com/33586189/48655637-3589c400-e9df-11e8-9cef-23df15798503.png">
