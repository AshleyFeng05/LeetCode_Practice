'''
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from typing import List

# Another important solution for Anagram problems is that sorted Anagram words should be the same
# So we create a dictionary to store each sorted word as the key, and corresponding unsorted words
# in a list as the value. For example, {"ant":["nat", "tan"]}.
# Here are the few mistakes should pay attention to:
# 1. The value in the dictionary is a list instead of string
# 2. Sorted(str) method will return a list instead of a string. ''.join(sorted(str)) is used to merge
# 3. Defaule dictionary will not automatically add a new key if being accessed with this key. You need 
#   to use if "key" in "map" logic or use defaultdict data structure instead.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupsDict = {}
        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word not in groupsDict:
                groupsDict[sorted_word] = [strs[i]]
            else:
                groupsDict[sorted_word].append(strs[i])
        return list(groupsDict.values())