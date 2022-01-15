class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index,num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num],index]
            hashmap[num] = index
#        print(hashmap)
        return None

sol = Solution()
print(sol.twoSum([2,7,11,15],17))
