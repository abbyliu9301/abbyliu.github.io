class Solution:
    def dfs(self, x, dic):
        if x in dic:
            for y in dic[x]:
                if y not in self.visited:
                    self.visited.add(y)
                    self.dfs(y, dic)


    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for x,y in edges:
            dic[x].append(y)
            dic[y].append(x)

        count = 0
        self.visited = set()
        for x in sorted(dic):
            if x not in self.visited:
                self.visited.add(x)
                self.dfs(x, dic)
                count += 1
        return count + n - len(sorted(dic))
