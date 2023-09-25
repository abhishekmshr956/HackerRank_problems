"""
https://leetcode.com/problems/koko-eating-bananas/
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""
class Solution:
    def totalHours(self, piles: list[int], speed: int) -> int:
        """ returns the number of hours (sessions) to eat all the bananas """
        H = 0
        for p in piles:
            H += (p + speed - 1) // speed
        return H

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = low + (high - low) // 2
            n = self.totalHours(piles, mid)
            if n <= h:
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == '__main__':
    # piles = [3, 6, 7, 11]; h = 8 # output 4
    # piles = [30,11,23,4,20]; h = 5 # output 30
    piles = [30,11,23,4,20]; h = 6 # output 23
    sol = Solution()
    print(sol.minEatingSpeed(piles, h))