class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num,0) + 1
        
        freq = [[] for _ in range(len(nums)+1)]

        for i, num in enumerate(counts):
            freq[i].append(num)
        res = []
        for i in range(len(nums)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
