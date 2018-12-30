# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        def generate(start, end):
            temp = []
            if start > end:
                temp.append(None)
            else:
                # i indicates the root node
                for i in range(start, end+1):
                    lefttree = generate(start, i-1)
                    righttree = generate(i+1, end)
                    for j in lefttree:
                        for k in righttree:
                            root = TreeNode(i)
                            root.left = j
                            root.right = k
                            temp.append(root)
            return temp
        return generate(1, n)

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        # i indicates the length 1 ~ i for the bst
        # using value j as the root
        # 1 ~ j-1 forms the left tree, j+1 ~ i forms the right tree
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]
