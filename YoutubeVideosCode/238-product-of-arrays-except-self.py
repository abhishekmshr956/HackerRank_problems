class Solution1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n
        left_products = [0] * n
        right_products = [0] * n

        left_product = 1 
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]

        for i in range(n):
            answer[i] = left_products[i] * right_products[i]

        return answer

# using one less array    
class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n
        left_products = [0] * n

        left_product = 1 
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] = left_products[i] * right_product
            right_product *= nums[i]

        return answer
    
# using only one array    
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [0] * n

        left_product = 1 
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer

if __name__ == '__main__':
    nums = [1,2,3,4] # Output = [24,12,8,6]
    sol = Solution()
    print(sol.productExceptSelf(nums))