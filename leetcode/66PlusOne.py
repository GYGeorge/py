# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-06 17:36:51 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-06 17:36:51 
#  */
#
#   leetcode id=61 lang=python
#
#   [61] Plus One
#
class Solution:
    @classmethod
    def plusOne(self, digits):
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        num += 1
        result = []
        while num != 0:
            n = num%10
            result.append(n)
            num = num//10
            result.reverse()
        return result
        
if __name__ == "__main__":
    digits = [4,2,2,1]
    print(Solution.plusOne(digits))
        