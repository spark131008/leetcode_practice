class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use sliding window technique
        # l, r = 0, 0
        # use hashMap to keep track of max frequency of a character
        # keep incrementing r-pointer until (window_size - max frequency) <= k
        # if not, then increment l-pointer and decrease s[l]'s frequency from the hashMap

        res = 1
        counterMap = {}
        l = 0

        for r in range(len(s)):
            counterMap[s[r]] = counterMap.get(s[r], 0) + 1

            if r - l + 1 - max(counterMap.values()) > k:
                counterMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

