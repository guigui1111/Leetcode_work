#Question 2:
#(Reverse Integer):
#Given a 32-bit signed integer, reverse digits of an integer.
#link: https://leetcode-cn.com/problems/reverse-integer/

class Solution:
    def reverInt(self,int):
        """
        :param int: 32-bit signed integer
        :return: int
        """
        my_return = ''
        if int == 0:
            return 0
        elif int < 0:
            my_return += '-'
        x = str(int)
        my_return += x[len(x)-1::-1].rstrip('-').lstrip('0')
        return my_return

answer = Solution()
print(answer.reverInt(-1240))


