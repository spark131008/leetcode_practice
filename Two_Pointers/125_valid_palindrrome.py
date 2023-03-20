import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile(r"[0-9a-zA-Z]+")
        char_list = pattern.findall(s)
        new_str = "".join(char_list).lower()

        left_pointer, right_pointer = 0, len(new_str)-1

        while left_pointer < right_pointer:
            if new_str[left_pointer] != new_str[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True

    def isPalindrome2(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s)-1

        while left_pointer < right_pointer:
            while left_pointer < right_pointer and not re.match(r"[0-9a-zA-Z]+", s[left_pointer]):
                left_pointer += 1
            while left_pointer < right_pointer and not re.match(r"[0-9a-zA-Z]+", s[right_pointer]):
                right_pointer -= 1
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            left_pointer += 1
            right_pointer -= 1
        return True