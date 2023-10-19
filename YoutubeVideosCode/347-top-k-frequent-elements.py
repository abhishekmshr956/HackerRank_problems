class Solution1:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        max_freq = max(freq_map.values())
        counts = [[] for _ in range(max_freq + 1)]

        for item, value in freq_map.items():
            counts[value].append(item)

        answer = []

        for i in range(len(counts) - 1, 0, -1):
            if counts[i]:
                answer.extend(counts[i])
                if len(answer) >= k:
                    return answer[:k]
                
        return answer
    

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = {}

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        counts = [[] for _ in range(len(nums) + 1)]

        for item, value in freq_map.items():
            counts[value].append(item)

        answer = []

        for i in range(len(counts) - 1, 0, -1):
            if counts[i]:
                answer.extend(counts[i])
                if len(answer) >= k:
                    return answer[:k]
                
            return answer

if __name__ == '__main__':
    # nums = [1,1,1,2,2,3]; k = 2 # Output: [1,2]
    nums = [7,3,4,4,3,7,7,3,7,3,6]; k = 3 # Output: [7,3,4]
    # nums = [1]; k = 1 # Output: [1]
    sol = Solution()
    print(sol.topKFrequent(nums, k))


