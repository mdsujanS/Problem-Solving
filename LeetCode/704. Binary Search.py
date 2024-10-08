# problem link - https://leetcode.com/problems/binary-search/description/
# Just implement the Binary Search Algorith

class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if(nums[middle] == target):
                return middle
            if target > nums[middle] :
                left = middle + 1
            else:
                right = middle - 1
        return -1