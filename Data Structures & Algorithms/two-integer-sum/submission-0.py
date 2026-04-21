class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i: int 
        # j: int
        # size = len(nums)
        # x: int = 0
        # y: int = 1
        # for num in nums:
        #     while y < size:
        #         if target == nums[x] + nums[y]:
        #             if x < y:
        #                 i = x
        #                 j = y
        #             elif y < x:
        #                 i = y
        #                 j = x
        #     y += 1
        # return [i, j]
        
        seen = {}
        
        for i, n in enumerate(nums):
            diff = target - n 
            if diff not in seen:
                seen[n] = i
            else:
                return [seen[diff], i]

        
        
        # vals = set(nums)
        # i:int
        # j:int 
        # for num in nums:
        #     diff = target - num
        #     if diff in vals:
        #         i = num
        #         j = diff
        #         return [i, j]
