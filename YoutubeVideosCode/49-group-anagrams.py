from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        
        for s in strs:
            counts = [0] * 26

            for char in s:
                counts[ord(char) - ord('a')] += 1

            res[tuple(counts)].append(s)

        return list(res.values())




if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"] # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs = [""] # Output: [[""]]
    strs = ["a"] # Output: [["a"]]
    sol = Solution()
    print(sol.groupAnagrams(strs))