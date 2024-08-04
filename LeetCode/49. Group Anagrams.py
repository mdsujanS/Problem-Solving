# Problem link -> https://leetcode.com/problems/group-anagrams/description/
# Time Complexity-> BigO(N * s log s)


from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        
        # defaultdict automatically creats a new list for any new key that doesn't exist in the dictionary.
        anagram_map = defaultdict(list)

        # List will hold the final result
        List = []
        for s in strs:

            # This convert the sorted list of characters into a tuple. Tuples are hashable and can be used as keys in a dictionary.
            sortString = tuple(sorted(s)) 

            # sorted tuple(key) is used to append the 's' to the list of string.
            anagram_map[sortString].append(s)

        for i in anagram_map.values():
            List.append(i)

        return List