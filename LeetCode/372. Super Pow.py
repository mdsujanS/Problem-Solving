# Problem link -> https://leetcode.com/problems/super-pow/description/
# Time Complexity -> O( k + log n) 'k' is the number of digit in b  


class Solution(object):
    def superPow(self, a, b):
        
        def powCalculate(a, n):

            result = 1

            while n > 0:
                if (n & 1):
                    result = (result * a) % 1337

                n = n >> 1
                a = (a * a) % 1337
            return result

        n = int("".join(list(map(str, b)))) # Converting list into integer
        ans = powCalculate(a, n)

        return ans

        
        