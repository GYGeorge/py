# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-03 23:56:40 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-03 23:56:40 
#  */
# leetcode id=204 lang=python3

class Solution:
    @classmethod
    def countPrimes(self, n: int):
        def isPrime(x):
            if x>1:
                for i in range(2,x):
                    if x % i == 0:
                        return False
                else:
                    return True
            else:
                return False
        nums = [0]*2 + [1]*(n-2)
        for i in range(2, int(n ** 0.5)+1):
            if isPrime(i):
                for j in range(i*i, n, i):
                    nums[j] = 0
        return sum(nums)
        
# if __name__ == "__main__":
#     print(Solution.countPrimes(100))
