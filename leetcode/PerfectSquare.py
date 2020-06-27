import math
import sys
class Solution:
    """ 
        给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
        使得它们的和等于 n。你需要让组成和的完全平方数的个数最少
    """
    def numSquares_dp(self, n: int):
        """动态规划"""
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 0
            while j ** 2 <= i:
                dp[i] = min(dp[i - j ** 2] + 1, dp[i])
                j += 1
        return dp[-1]
    
    
    def numSquares_ga(self, n: int):
        
        def is_divided_by(n, count):
            """
                递归
                如果n可以分成count个完全平方数,返回True
                e.g. n=12, count=3:  true.
                     n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums
            
            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])
    
        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count
    
    
    def numSquares_ga_bfs(self, n):
        """
            用广度优先(即队列)的方法来计算
        """
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
        level = 0
        queue = {n}
        while queue:
            level += 1
            # 用set以消除冗余
            next_queue = set()
            # 计算下一层的队列
            for r in queue:
                for num in square_nums:    
                    if r == num:
                        return level
                    elif r < num:
                        break
                    else:
                        next_queue.add(r - num)
            queue = next_queue
        return level
    
    
    
    def isSquare(self, n: int):
        """
            是否是平方数返回bool类型
        """
        sq = int(math.sqrt(n))
        return sq*sq == n

    def numSquares_math(self, n: int):
        """
            四平方和定理(Lagrange's four-square theorem)
        """
        # n == 4 ** k * (8 * m + 7)
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if self.isSquare(n):
            return 1
        
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3
    
    
    
if __name__ == "__main__":
    x = int(input("input number: "))
    solution = Solution()
    print(solution.numSquares_dp(x))
    print(solution.numSquares_ga(x))
    print(solution.numSquares_ga_bfs(x))    
