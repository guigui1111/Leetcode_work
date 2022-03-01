#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = list(s), list(t)
        a.sort()
        b.sort()
        return a == b
        #方法2：
        # return Counter(s) == Counter(t)
        #方法3：
        # dict1, dict2 = {}, {}
        # for i in range(len(s)):
        #     if s[i] in dict1:
        #         dict1[s[i]] += 1
        #     else:
        #         dict1[s[i]] = 1
        # for j in range(len(t)):
        #     if t[j] in dict2:
        #         dict2[t[j]] += 1
        #     else:
        #         dict2[t[j]] = 1
        # return dict1==dict2

# 作者：ruo-nian-feng-chen
# 链接：https://leetcode-cn.com/problems/valid-anagram/solution/pythonsan-chong-fang-fa-by-ruo-nian-feng-ej5c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


sol = Solution()
print(sol.isAnagram(s = "anagram", t = "nagaram"))