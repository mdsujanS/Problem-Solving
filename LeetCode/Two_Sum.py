# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lenList = len(nums)
        for i in range(lenList):
            for j in range(i+1, lenList):
                if(nums[i] + nums[j] == target):
                    return [i, j]
        return []   

