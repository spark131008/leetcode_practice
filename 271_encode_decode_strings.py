from typing import List

class Solution:
    def encode(self, strs: List) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str) -> List:
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j+1:j+1+length])
            i = j + 1 + length
        return res

    def decode2(self, str) -> List:
        res, i = [], 0

        while i < len(str):
            for char_index in range(len(str)):
                if str[char_index] == "#":
                    length = int(str[i:char_index])
                    res.append(str[char_index+1:char_index+1+length])
                    i = char_index + length + 1
        return res