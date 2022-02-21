# Question 5:
# (Longest Common Prefix):
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# link: https://leetcode-cn.com/problems/longest-common-prefix/

class Solution:
    def maxPre(self, array1):
        """
        :param array1:
        :return: string
        """
        s1 = min(array1)
        s2 = max(array1)
        # print(s1)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]


sol = Solution()
print(sol.maxPre(["flower", "flow", "flight"]))