from typing import List

class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            res[n] = 1 + res.get(n, 0)

        sorted_res = sorted(res.items(), key=lambda item: item[1], reverse=True)
        final_res = []
        for key, value in sorted_res[:k]:
            final_res.append(key)
        return final_res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res