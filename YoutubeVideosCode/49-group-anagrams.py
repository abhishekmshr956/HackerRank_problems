from collections import defaultdict

# time complexity O(n * k); n is len(strs); k is the maximum length of a string in the input 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        
        for word in strs:
            counts = [0] * 26

            for char in word:
                counts[ord(char) - ord('a')] += 1

            key = tuple(counts)

            if key not in anagrams:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)

        return list(anagrams.values())
    

# time complexity O(n * k * log(k)); n is len(strs); k is the maximum length of a string in the input    
class Solution1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        return list(anagrams.values())

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"] # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    # strs = [""] # Output: [[""]]
    # strs = ["a"] # Output: [["a"]]
    sol = Solution()
    print(sol.groupAnagrams(strs))