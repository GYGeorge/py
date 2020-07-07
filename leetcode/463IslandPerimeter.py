#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    @classmethod
    def islandPerimeter(self, grid):
        edge = 0
        block = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                if i > 0 and grid[i-1][j]:
                    edge += 1
                if j > 0 and grid[i][j-1]:
                    edge += 1
                block += 1
        print(block)
        print(edge)
        return block * 4 - edge * 2
    
if __name__ == "__main__":
    inputmap = [[0,1,0,0],
                [1,1,1,0],
                [0,1,0,0],
                [1,1,0,0]]
    print(Solution.islandPerimeter(inputmap))
# @lc code=end

