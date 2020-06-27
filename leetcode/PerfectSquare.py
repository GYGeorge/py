import math
import sys
class Solution:
    """ 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
        使得它们的和等于 n。你需要让组成和的完全平方数的个数最少"""
    def numSquares_dp(self, n: int):
        """动态规划"""
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 0
            while j ** 2 <= i:
                dp[i] = min(dp[i-j**2]+1, dp[i])
                j += 1
        return dp[-1]
    
if __name__ == "__main__":
    x = int(input("input number: "))
    solution = Solution()
    print(solution.numSquares_dp(x))
        
