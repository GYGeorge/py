#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#

# @lc code=start
class Solution:
    # @classmethod
    def prisonAfterNDays(self, cells, N: int):
        cycle = N % 14
        if cycle == 0:
            cycle = 14
        newcell = cells
        for j in range(cycle):
            temp = [0]
            for i in range(1,7):
                if newcell[i - 1] == newcell[i + 1]:
                    temp.append(1)
                else:
                    temp.append(0)
            temp.append(0)
            newcell = temp
        return newcell    
        


# if __name__ == '__main__':
#     array = [0,1,0,1,1,0,0,1]
#     array2= [1,0,0,1,0,0,1,0]
#     result = Solution.prisonAfterNDays(array2, N=1000000000)
#     print(result)
    
