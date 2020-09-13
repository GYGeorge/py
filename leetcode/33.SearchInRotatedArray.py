# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-09-13 10:40:43 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-09-13 10:40:43 
#  */
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2 )
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]:
                if nums[left] <= target and nums[mid] > target:
                    right = mid - 1 
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid -1
        if nums[left] == target:
            return left
        return -1
    