# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-05 20:29:00 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-05 20:29:00 
#  */
#
# leetcode id=491 lang=python
#
# [491] Hamming Distance
#
class Solution:
    @classmethod
    def hammingDistance(self, x: int, y: int):
        m = x ^ y
        count = 0
        while m != 0:
            if (m & 0x01) == 0x01:
                count += 1
            m >>= 1
        return count
    
if __name__ == "__main__":
    Solution.hammingDistance(4, 2)
    