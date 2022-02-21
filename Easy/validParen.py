#Question 6:
#(Valid Parentheses):
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid
#link: https://leetcode-cn.com/problems/valid-parentheses/
class Solution:
    def isValidP(self,string1):
        """
        :param string1: string
        :return: True of False
        """
        while '()' in string1 or '{}' in string1 or '[]' in string1:
            string1 = string1.replace('()', '')
            string1 = string1.replace('{}', '')
            string1 = string1.replace('[]', '')
        return string1 == ''



sol = Solution()
print(sol.isValidP("{[]}"))