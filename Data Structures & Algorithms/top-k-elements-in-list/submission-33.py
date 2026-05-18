class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        print(count,freq)
        for i in range(len(nums), -1, -1):
            for j in freq[i]:
                print(i,j,res)
                if len(res) == k:
                    return res
                res.append(j)            
        return res