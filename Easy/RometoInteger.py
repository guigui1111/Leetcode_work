#Question 4:
#(Roman to Integer):
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#link: https://leetcode-cn.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self,roman):
        """
        :param roman: string
        :return: int
        """
        my_dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        my_return = 0
        for i in range(len(roman)):
            if i < len(roman)-1 and my_dic[roman[i]] < my_dic[roman[i+1]]:
                my_return -= my_dic[roman[i]]
            else:
                my_return += my_dic[roman[i]]
        return my_return

my_sol = Solution()
print(my_sol.romanToInt('XIV'))


