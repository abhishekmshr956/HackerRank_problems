import heapq
import math
from typing import List

#using minheap
class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        answer = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(points_heap, (distance, point))

        for i in range(k):
            smallest_point = heapq.heappop(points_heap)[1]
            answer.append(smallest_point)

        return answer
    
# using maxheap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closest = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if len(k_closest) < k:
                heapq.heappush(k_closest, (-distance, point))
            else:
                if -distance > k_closest[0][0]:
                    heapq.heappop(k_closest)
                    heapq.heappush(k_closest, (-distance, point))

        return [point for (_, point) in k_closest]
    
#using minheap and using heapify instead of heappush
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        answer = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            points_heap.append((distance, point))

        heapq.heapify(points_heap)
        for i in range(k):
            smallest_point = heapq.heappop(points_heap)[1]
            answer.append(smallest_point)

        return answer





if __name__ == '__main__':
    # points = [[1,3],[-2,2]]; k = 1 # Output: [[-2,2]]
    # points = [[3,3],[5,-1],[-2,4]]; k = 2 # Output: [[3,3],[-2,4]]
    points = [[1,3],[-2,2],[2,-2]]; k = 2  # Output: [[-2,2],[2,-2]]
    sol = Solution()
    print(sol.kClosest(points, k))