# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-04 15:46:32 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-04 15:46:32 
#  */
#
# leetcode id=264 lang=python
#
# [264] Ugly Number 2
#

class Solution:
    @classmethod
    def nthUglyNumber(self, n: int):
        """
            动态规划求解
        """
        if n == 1:
            return 1
        numslist = [1]
        index2=index3=index5 = 0
        i = 0
        while i != n-1:
            num = min(numslist[index2] * 2, numslist[index3] * 3, numslist[index5] * 5)
            numslist.append(num)
            if num == numslist[index2]*2:
                index2 += 1
            if num == numslist[index3]*3:
                index3 += 1
            if num == numslist[index5]*5:
                index5 += 1
            i += 1
        return numslist[n-1]
    
if __name__ == "__main__":
    print(Solution.nthUglyNumber(10))