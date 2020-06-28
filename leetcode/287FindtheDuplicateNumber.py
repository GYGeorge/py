class Solution:
    """
        Given an array nums containing n + 1 integers 
        where each integer is between 1 and n (inclusive), 
        prove that at least one duplicate number must exist. 
        Assume that there is only one duplicate number, find the duplicate one.
    """
    def FindtheDuplicateNumber(self, nums):
        """
            环检测算法Floyd's the Tortoise and Hare
        """
        hare = tortoise = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if hare == tortoise:
                break
        hare = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return hare
    
if __name__ == "__main__":
    array = [3,1,3,4,2]
    so = Solution()
    print(so.FindtheDuplicateNumber(array))