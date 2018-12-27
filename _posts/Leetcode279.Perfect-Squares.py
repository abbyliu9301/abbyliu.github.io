class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        upper = int(math.sqrt(n)) + 1
        l = [i**2 for i in range(1, upper)]
        queue = collections.deque()
        # queue stores minimum level with remaining target
        queue.append((0, n))
        visited = {n}
        while queue:
            count, target = queue.popleft()
            for num in l:
                if target - num < 0:
                    break
                if target - num == 0:
                    return count + 1
                if target - num > 0 and (target - num) not in visited:
                    visited.add(target - num)
                    queue.append((count + 1, target - num))
