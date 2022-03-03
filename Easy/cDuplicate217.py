##Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        numset = {}
        for i in nums:
            if i not in numset:
                numset[i]=1
            else:
                return True
        return False


    def containsDuplicate2(self, nums):
        return len(nums) != len(set(nums))

    def containsDuplicate3(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

my_sol = Solution()
print(my_sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(my_sol.containsDuplicate([3,4,2]))

#https://leetcode-cn.com/problems/contains-duplicate/solution/cun-zai-zhong-fu-de-yuan-su-yi-yi-ti-san-ihfa/


