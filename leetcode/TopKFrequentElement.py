# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-17 17:26:23 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-17 17:26:23 
#  */
class Solution:
    @classmethod
    def topKFrequent(self, nums: list, k: int):
        dic = {}
        for i in nums:
            dic[i] = dic[i] + 1 if i in dic else 1
        dic = sorted(dic.items(), key=lambda kv:kv[1], reverse=True)
        res = []
        for i in range(k):
            res.append(dic[i][0])
        return res

if __name__ == "__main__":
    array = [1,2,3,1,1,1,3,5,4,6,3,2,3,1,3,3,3,3]
    print(Solution.topKFrequent(array, 3))
        