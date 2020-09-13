# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-09-13 09:53:51 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-09-13 09:53:51 
#  */
class Solution:
    def findMin(self, nums):
        if not nums:
            return []
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:#l < r 有序直接返回
                return nums[left]
            mid = int(left + (right - left) / 2)
            if nums[mid] > nums[right]:#mid > l 直接抛弃有序的
                left = mid + 1
            else:
                right = mid
        return nums[left]
            
if __name__ == "__main__":
    a = Solution()
    nums = [2,1]
    print(a.findMin(nums))
    