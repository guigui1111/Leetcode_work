#Question 3:
#(Palindrome Number):
#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#link: https://leetcode-cn.com/problems/palindrome-number/

class Solution:
    def palindrome(self,int):
        """
        :param int: int
        :return:
        """
        if int < 0:
            return none
        else:
            str_int = str(int)
            if str_int == str_int[len(str_int)-1::-1]:
                return 'yes'

my_sol = Solution()
print(my_sol.palindrome(3532))


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            y = str(x)[::-1]
            if y == str(x):
                return True
            else:
                return False