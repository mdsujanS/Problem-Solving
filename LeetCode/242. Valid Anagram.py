# problem link-> https://leetcode.com/problems/valid-anagram/description/
# Time Complexity  -> BigO(n + m)


from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        count_freq = defaultdict(int)

        # O(n)
        for ch in s:
            count_freq[ch] += 1

        # O(m)
        for ch in t:
            count_freq[ch] -= 1
            
        # O(n + m)
        for char in count_freq.values():
            if char != 0:
                return False
            
        return True