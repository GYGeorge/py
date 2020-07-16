# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-16 20:26:23 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-16 20:26:23 
#  */
# leetcode id=50 lang=python
# [50] Pow(x,n)
class Solution:
    @classmethod
    def myPow(self, x:float, n:int):
        def rec(recX: float, recN: int):
            if not recN:
                return 1
            if recN == 1:
                return recX
            res = rec(recX, recN / 2)
            if not recN % 2:
                return res * res
            return res * res * recX
        
        if n < 0:
            n = -n
            x = 1 / x
        return rec(x, n)