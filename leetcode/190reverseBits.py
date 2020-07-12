# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-12 15:48:02 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-12 15:48:02 
#  */
#
# leetcode id=190 lang=python
#
# [190] Reverse Bits

class Solution:
    @classmethod
    def reverseBits(self, n: int):
        res = 0
        for i in range(32):
            num = n & 0x00000001
            n >>= 1
            res <<= 1
            res = res | num
        return res
        
if __name__ == "__main__":
    n = 0b00001100001100001101000100101111
    print(bin(Solution.reverseBits(n)))