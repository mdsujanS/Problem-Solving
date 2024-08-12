# Problem link - https://leetcode.com/problems/powx-n/description/
# Time Complexity - O(log n)


class Solution(object):
    def myPow(self, x, n):

        def powCalculate(x , n):
            result = 1
            while n > 0:
                # If n is odd multiply x with result
                if (n & 1):
                    result = result * x
                n = n >> 1
                x = x * x   # Change x to x^2
            return result

        ans = powCalculate(x, abs(n))
        if n >= 0:
            return ans
        else:
            return 1 / ans
        