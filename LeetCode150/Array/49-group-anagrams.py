"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

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
"""
# def count(s):
#     count = {}
#     for i in s:
#         count[i] = count.get(i, 0) + 1
#     return count

def groupAnagrams(strs):
    res = {}
    for s in strs:
        count = [0] * 26 # a .... z
        for c in s:
            count[ord(c) - ord("a")] += 1
        key = tuple(count)
        if key in res:
            res[key].append(s)
        else:
            res[key] = [s]
    
    return list(res.values())
    



# def isAnagram(s, t):
#     freq_s = {}
#     freq_t = {}

#     for i in s:
#         freq_s[i] = freq_s.get(i, 0) + 1
#     for i in t:
#         freq_t[i] = freq_t.get(i, 0) + 1
#     return freq_s == freq_t

# def groupAnagrams(strs):
#     output = [[strs[0]]]
#     for s in strs[1:]:
#         flag = False
#         for i in range(len(output)):
#             if isAnagram(s, output[i][0]):
#                 output[i].append(s)
#                 flag = True
#                 break
#         if flag == False:
#             output.append([s])
#     return output

# def freq_map(s):
#     freq_s = {}
#     for i in s:
#         freq_s[i] = freq_s.get(i, 0) + 1
#     return freq_s

# def freq_maps(strs):
#     strs_freq_maps = []
#     for s in strs:
#         strs_freq_maps.append(freq_map(s))
#     return strs_freq_maps

# def groupAnagrams1(strs):
#     output = [[strs[0]]]
#     for s in strs[1:]:
#         if is

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    # strs = [""]
    # strs = ["a"]
    print(groupAnagrams(strs))