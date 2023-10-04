class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charCount_s = {}
        charCount_t = {}

        for i in range(len(s)):
            charCount_s[s[i]] = charCount_s.get(s[i], 0) + 1
            charCount_t[t[i]] = charCount_t.get(t[i], 0) + 1

        return charCount_s == charCount_t
    
if __name__ == '__main__':
    s = "anagram"; t = "nagaram" #Output: true
    s = "rat"; t = "car" # Output False
    sol = Solution()
    print(sol.isAnagram(s, t))