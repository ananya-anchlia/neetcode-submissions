class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            frequency[n] = 1 + frequency.get(n, 0)
        
        arr = []
        for n, cnt in frequency.items():
            arr.append([cnt, n])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
