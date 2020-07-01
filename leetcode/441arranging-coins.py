# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-01 17:03:46 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-01 17:03:46 
#  */
#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
import math
# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
            数学运算
        """
        n = n<<3
        return int((math.sqrt(n + 1) - 1) / 2)

