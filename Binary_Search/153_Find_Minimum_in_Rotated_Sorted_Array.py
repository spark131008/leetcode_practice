from typing import List
import sys


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = sys.maxsize
        l, r = 0, len(nums) - 1

        while nums[l] > nums[r]:
            m = l + (r - l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        res = min(res, nums[l])
        return res
