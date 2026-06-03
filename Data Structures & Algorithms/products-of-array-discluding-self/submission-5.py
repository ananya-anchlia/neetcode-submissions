class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product: int = 1
        final: list[int] = []
        zeroCount: int = 0
        for n in nums:
            if n != 0:
                product = product * n
            else:
                zeroCount += 1
        for n in nums:
            if n == 0:
                if zeroCount > 1:
                    final.append(0)
                else:
                    final.append(int(product))
            else:
                if zeroCount >= 1:
                    final.append(0)
                else:
                    final.append(int(product/n))
        return final