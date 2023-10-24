import heapq
from typing import List

# using heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = []
        for num in nums:
            if len(k_largest) < k:
                heapq.heappush(k_largest, num)
            else:
                if num > k_largest[0]:
                    heapq.heappop(k_largest)
                    heapq.heappush(k_largest, num)

        return heapq.heappop(k_largest)

import random   
#using quickSelect
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right):
            pivot = random.randint(left, right)
            nums[right], nums[pivot] = nums[pivot], nums[right]
            pivot_value = nums[right]
            store_index = left
            for i in range(left, right):
                if nums[i] > pivot_value:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            nums[store_index], nums[right] = nums[right], nums[store_index]
            return store_index
        
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_index = partition(nums, left, right)
            if pivot_index == k - 1:
                return nums[pivot_index]
            elif pivot_index < k - 1:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

