
# problem link-> https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
#  Time Complexity - BigO(NlogN)

class Solution(object):
    def maxOperations(self, nums, k):

        nums.sort()
        ans = 0
        i = 0 
        j = len(nums) - 1

        while i < j:
            locSum = nums[i] + nums[j]

            if locSum == k:
                ans+=1
                i+=1
                j-=1
            elif locSum > k:
                j-= 1
            else:
                i+=1
        return ans
        


