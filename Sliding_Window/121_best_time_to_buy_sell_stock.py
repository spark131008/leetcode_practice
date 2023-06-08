from typing import List


class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        l, r = 0, 1  # buying = left, selling = right
        res = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1
        return res

    def maxProfit_2(self, prices: List[int]) -> int:
        res = 0

        lowestP = prices[0]
        for p in prices:
            if p < lowestP:
                lowestP = p
            res = max(res, p - lowestP)
        return res
