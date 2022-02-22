#Question 8:
#(Remove Duplicates from Sorted Array):
#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#link: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        """
        :param list1: list of int
        :return: int for new list length
        """
        ans = []
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                ans.append(nums[i])
        ans.append(nums[len(nums) - 1])
        return ans


sol = Solution()
print(sol.removeDuplicates([1,1,2,2,3,5,7,34,67]))

class Solution:
    def removeDuplicates(self, nums):
        pre,cur=0,1
        while cur<len(nums):
            if nums[pre]==nums[cur]:
                nums.pop(cur)
                #print(nums)
            else:
                pre,cur=pre+1,cur+1
        return len(nums)

#作者：george-26
#链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/python-gan-jue-wo-de-si-lu-zui-jian-dan-by-george-/

class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

#作者：jyd 双指针
#链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/remove-duplicates-from-sorted-array-shuang-zhi-zhe/
