#O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap= {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap: 
                return [prevMap[diff], i]
            else:
                prevMap[nums[i]] = i



#O(n^2)
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                

if __name__ == '__main__':
    nums = [2,7,11,15]; target = 9 #Output: [0,1]
    s = Solution()
    print(s.twoSum(nums, target))
    s1 = Solution1()
    print(s1.twoSum(nums, target))