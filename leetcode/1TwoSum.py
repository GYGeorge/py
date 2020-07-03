# /*
#  * @Author: gaoyuan
#  * @Date: 2020-07-03 23:21:44
#  * @Last Modified by:   gaoyuan
#  * @Last Modified time: 2020-07-03 23:21:44
#  */
# leetcode id = 1, lang=python3
#
# [1] Two Sum
#


class Solution:
    @classmethod
    def twoSum(self, nums, target: int):
        """
            hashmap{value : key}
            when nums = [2,7,9,10]
            ashmap = {2:0, 7:1, 9:2, 10:3}
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return (dict[target-x] + 1, i + 1)
            dict[x] = i


# if __name__ == "__main__":
#     nums = [2,7,9,10]
#     target = 16
#     print(Solution.twoSum(nums,target))
