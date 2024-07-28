# problem link- https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# >>> Sliding Window Approach



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        stringLen = len(s)
        substringLength = 0
        substring = set()
        i, j= 0, 0

        while j < stringLen:

            if s[j] not in substring:
                substring.add(s[j])
                substringLength = max(substringLength, j - i + 1)
            else:
                while s[j] in substring:
                    substring.remove(s[i])
                    i+=1
                substring.add(s[j])
            j+=1

        return substringLength
    
