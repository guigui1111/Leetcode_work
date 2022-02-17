#Question 2:
#(Reverse Integer):
#Given a 32-bit signed integer, reverse digits of an integer.
#link: https://leetcode-cn.com/problems/reverse-integer/

class Solution:
    def reversInt(self, int):
        """
        :param int: 32-bit
        :return: int
        """
        if int == 0:
            return 0
        string_int = str(int)
        my_return = ''
        if string_int[0] == '-':
            my_return +='-'
        else:
            my_return += string_int[len(int)-1::-1].lstrip('0')
            print(my_return)
            #my_return = int(my_return)
            print(my_return)
        return my_return

sol = Solution()
print(sol.reversInt('8637'))



class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x ==0:
            return 0
        str_x = str(x)
        x=''
        if str_x[0] == '-':
            x+= '-'
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")
        x= int(x)
        if -2**31<x<2**31-1:
            return x
        return 0



class Solution:
    def reverInt(self, int):
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
        my_return += x[len(x) - 1::-1].rstrip('-').lstrip('0')
        return my_return

answer = Solution()
print(answer.reverInt(-1240))

