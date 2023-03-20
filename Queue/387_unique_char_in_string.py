from collections import deque, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = deque(s)

        for i in range(len(s)):
            char = d.popleft()
            if not char in d:
                return s.index(char)
            else:
                d.append(char)
        return -1

    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for inx, char in enumerate(s):
            if count[char] == 1:
                return inx
        return -1