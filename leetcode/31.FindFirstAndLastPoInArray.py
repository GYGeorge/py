# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-09-13 12:50:32 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-09-13 12:50:32 
#  */

class Solution:
    @classmethod
    def searchRange(self, nums, target) :
        left = 0
        right = len(nums) - 1
        res = []
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:#找左边
                right = mid
            else:
                left = mid + 1
        res.append(left)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:#找右边
                right = mid 
            else:
                left = mid + 1
        if nums[left] == target:
            res.append(left)
        else:
            res.append(left - 1)
        if res[0] > res[1]:
            return [-1,-1]
        return res
    
if __name__ == "__main__":
    array = [1]
    target = 1
    print(Solution.searchRange(array,target))