from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, n in enumerate(nums):
            next_n = target - n
            if next_n in res:
                return [i, res.get(next_n)]
            res[n] = i
