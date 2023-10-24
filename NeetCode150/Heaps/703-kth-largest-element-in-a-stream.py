import heapq 
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            if val > self.min_heap[0]:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, val)
        return self.min_heap[0]
    
if __name__ == '__main__':
    kthLargest = KthLargest(3, [4,5,8,2])
    print(kthLargest.add(3)) # Output: 4
    print(kthLargest.add(5)) # Output: 5
    print(kthLargest.add(10))  # Output: 5
    print(kthLargest.add(9))  # Output: 8
    print(kthLargest.add(4))  # Output: 8

