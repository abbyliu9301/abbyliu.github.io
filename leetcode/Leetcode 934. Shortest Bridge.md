# Leetcode 934. Shortest Bridge

## Problem Setting

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)


## Example 

Input: [[0,1],[1,0]]\
Output: 1

Input: [[0,1,0],[0,0,0],[0,0,1]]\
Output: 2

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]\
Output: 1

## Thinking Process

This is a graph problem, so probably BFS or DFS should be used. Since we're trying to find the minimum number of 0s between the two bridges (shortest path), it would be natural to do the search level by level expanding from 1s and BFS is more appropriate here. **The tricky part is, what is the starting point?** Instead of starting from all 1s, we should start from the boundary of one bridge and try to reach the other bridge. First, find the first bridge and mark its boundary, and then search from its boundary layer by layer until another bridge is met.

<img width="721" alt="screen shot 2018-11-14 at 8 15 26 pm" src="https://user-images.githubusercontent.com/33586189/48526069-e52e2d00-e84b-11e8-9c85-2b880c3f39d9.png">

<img width="721" alt="screen shot 2018-11-14 at 8 15 56 pm" src="https://user-images.githubusercontent.com/33586189/48526088-f5460c80-e84b-11e8-95d7-6b17849b1674.png">

