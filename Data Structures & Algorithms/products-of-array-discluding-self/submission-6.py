class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product: int = 1
        zeroCount: int = 0
        final: List[int] = []
        for n in nums:
            if n == 0:
                zeroCount += 1
                if zeroCount > 1:
                    product = 0
            else:
                product = product * n
        for n in nums:
            if zeroCount > 1:
                final.append(product)
            elif zeroCount == 1:
                if n == 0:
                    final.append(int(product))
                else:
                    final.append(0) 
            else:
                final.append(int(product/n))
        return final

        

        