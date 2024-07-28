# problem link - https://leetcode.com/problems/maximum-ascending-subarray-sum/


class Solution(object):
    def maxAscendingSum(self, nums):
        listLength = len(nums)
        maxSum = 0
        listSum = nums[0]
        for i in range(1, listLength):

            if nums[i-1] < nums[i]:
                listSum+= nums[i]
            
            else:
                maxSum = max(maxSum, listSum)
                listSum = nums[i]
        maxSum = max(maxSum, listSum)

        return maxSum
