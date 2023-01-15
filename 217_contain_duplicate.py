from typing import List

class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        num_len = len(nums)
        distinct_num_len = len(set(nums))
        print(distinct_num_len)
        return True if num_len != distinct_num_len else False

    def containDuplicate2(self, nums: List[int]) -> bool:
        hash_set = set()

        for n in nums:
            if n in hash_set:
                return True
            hash_set.add(n)
        return False