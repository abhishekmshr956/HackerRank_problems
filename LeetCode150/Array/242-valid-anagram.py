""" https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # solution using 2 hash maps

        if len(s) != len(t):
            return False
            
        freq_map_s = {}
        freq_map_t = {}
        for i in s:
            freq_map_s[i] = freq_map_s.get(i, 0) + 1
        for i in t:
            freq_map_t[i] = freq_map_t.get(i, 0) + 1

        return freq_map_s == freq_map_t
        

        # # solution using single hash map
        # freq_map = {}
        # for i in s:
        #     freq_map[i] = freq_map.get(i, 0) + 1
        # for i in t:
        #     freq_map[i] = freq_map.get(i, 0) - 1
        
        # for key, value in freq_map.items():
        #     if value != 0:
        #         return False
        # return True
    
if __name__ == '__main__':
    sol = Solution()
    s = "anagram"
    t = "nagaram" # output = True
    s = "rat"; t = "car" # output = False
    print(sol.isAnagram(s, t))
