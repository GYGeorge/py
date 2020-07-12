# /*
#  * @Author: gaoyuan
#  * @Date: 2020-07-08 22:04:28
#  * @Last Modified by:   gaoyuan
#  * @Last Modified time: 2020-07-08 22:04:28
#  */
#
#  leetcode id= lang=python
#
#   [] 3Sum
#


class Solution:
    @classmethod
    def threeSum(self, nums):
        nums.sort()
        res = []
        k = 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if  k > 0 and nums[k] == nums[k-1]:
                continue
            i,j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[i] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res 
    
if __name__ == "__main__":
    array = [-1,0,1,2,-1,-4]
    print(Solution.threeSum(array))
        