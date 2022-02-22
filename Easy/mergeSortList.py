# Question 7:
# (Merge Two Sorted Lists):
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# link: https://leetcode-cn.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeSortList(self, list1, list2):
        """
        :param list1: list of int
        :param list2: list of int
        :return: list of int
        """
        list3 = list1 + list2
        list3.sort()
        return list3

mysol = Solution()
print(mysol.mergeSortList([1, 2, 4], [1, 3, 4]))

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class Solution:
    def mergeSortList(self, list1, list2):
        """
        :param list1: list of int
        :param list2: list of int
        :return: list of int
        """
        new1 = new2 = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                new2.next = list1
                list1 = list1.next
            else:
                new2.next = list2
                list2 = list2.next
            new2 = new2.next
        new2.next = list1 or list2
        return new1.next

mysol = Solution()
print(mysol.mergeSortList([1, 2, 4], [1, 3, 4]))

