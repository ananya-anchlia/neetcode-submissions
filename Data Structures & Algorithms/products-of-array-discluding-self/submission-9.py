class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final = [1] * n
        
        # Pass 1: Calculate prefixes (Left to Right)
        # Every slot gets the product of everything to its left
        prefix = 1
        for i in range(n):
            final[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Calculate suffixes (Right to Left)
        # Multiply what's already in 'final' by everything to its right
        suffix = 1
        for i in range(n - 1, -1, -1):
            final[i] *= suffix
            suffix *= nums[i]
            
        return final