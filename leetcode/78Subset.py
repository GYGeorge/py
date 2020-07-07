# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-06 22:08:37 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-06 22:08:37 
#  */
#
# leetcode id=78 lang=python
#
# [78] Subsets
#
class  Solution:
    @classmethod
    def subsets(self, sets):
        subsets = []
        for i in range(1<<len(sets)):
            temp = []
            for j in range(len(sets)):
                if (i >> j) & 1:
                    temp.append(sets[j])
            subsets.append(temp)
        print(subsets)
        
if __name__ == "__main__":
    array = [4,5,7]
    Solution.subsets(array)
                
            