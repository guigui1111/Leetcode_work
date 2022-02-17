#Question 1:
#(two sum):
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#link: https://leetcode-cn.com/problems/two-sum/

##First way
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index,num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                print(another_num)
                return [hashmap[another_num],index]
            hashmap[num] = index
            print(hashmap)
        return None

sol = Solution()
print(sol.twoSum([2,7,11,15],18))


##second way
class Solution:
    def twoSum(self, nums, target):
        """
        :param nums: array of ints
        :param target: int
        :return: list[int]
        """
        indicesList = {}
        for index, num in enumerate(nums):
            if target - num in nums:
                #print([index, num])
                #print(nums.index(target-num))
                return [index, nums.index(target-num)]

sol = Solution()
#print(sol.twoSum([2, 7, 11, 15],18))

