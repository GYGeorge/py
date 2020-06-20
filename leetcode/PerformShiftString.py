class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [0]*length
        output[0] = 1
        help = 1
        for i in range(1,length):
            output[i] = output[i - 1] * nums[i - 1]
        for i in reversed(range(length)):
            output[i] = output[i] * help
            help = help * nums[i]
        return output



