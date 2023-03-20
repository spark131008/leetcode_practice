from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            sortedString = ''.join(sorted(string))
            res[sortedString].append(string)
        return res.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()