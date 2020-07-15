# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-15 16:33:00 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-15 16:33:00 
#  */
#
# leetcode id= lang=python
#
# [] Reverse Words In A Sting

class Solution:
    @classmethod
    def reverseWords(self, s: str):
        de = s.split()
        output = ""
        for i in reversed(de):
            output += " " + i
        return output[1:]
    
if __name__ == "__main__":
    r = "a wowo de s "
    print(Solution.reverseWords(r))