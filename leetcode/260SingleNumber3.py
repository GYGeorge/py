#  /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-23 22:06:40 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-23 22:06:40 
#  */

class Solution:
    def singleNumber(self, nums: int):
        """
            bit manipulation
        """
        s = 0
        for n in nums:
            s ^= n
            
        different = s & (-s)#找到s最右侧的1
        x = 0
        for n in nums:
            if n & different:#除去了y, 即y不满足该if语句
                x ^= n
        return [x, s^x]        
        