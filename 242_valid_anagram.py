class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)):
            s_hashmap[s[i]] = 1 + s_hashmap.get(s[i], 0)
            t_hashmap[t[i]] = 1 + t_hashmap.get(t[i], 0)
        return s_hashmap == t_hashmap

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = []
        t_list = []

        for i in range(len(s)):
            s_list.append(s[i])
            t_list.append(t[i])

        s_list.sort()
        t_list.sort()

        return s_list == t_list