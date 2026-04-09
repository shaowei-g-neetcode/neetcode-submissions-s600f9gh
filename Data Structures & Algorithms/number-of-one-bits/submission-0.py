class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            # 每次把最右邊的一個 1 消掉
            n = n & (n - 1)
            count += 1

        return count