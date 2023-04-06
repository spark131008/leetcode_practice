from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r
        while l <= r:
            m = (l + r) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p / m)

            if hour <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res