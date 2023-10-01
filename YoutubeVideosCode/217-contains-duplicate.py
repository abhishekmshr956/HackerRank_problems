class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        uniqueElements = set()
        for n in nums:
            if n in uniqueElements:
                return True
            else:
                uniqueElements.add(n)
        return False
    
if __name__ == '__main__':
    nums = [1,2,3,1] # true
    nums = [1,2,3,4] # false
    nums = [1,1,1,3,3,4,3,2,4,2] # true
    s = Solution()
    print(s.containsDuplicate(nums))