from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                seq_length = 0
                while (n + seq_length) in numSet:
                    seq_length += 1
                longest = max(longest, seq_length)
        return longest