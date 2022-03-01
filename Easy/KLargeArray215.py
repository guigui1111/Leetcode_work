##Given an integer array nums and an integer k, return the kth largest element in the array.
#Note that it is the kth largest element in the sorted order, not the kth distinct element.
##https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/215-shu-zu-zhong-de-di-kge-zui-da-yuan-s-wo4c/


class Solution:
    def findKthLargest(self, nums, k: int):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        nums.sort(reverse=True)
        print(nums)
        return nums[k-1]


#and more soluiton

my_sol = Solution()
print(my_sol.findKthLargest([3,2,1,5,6,4], 2))