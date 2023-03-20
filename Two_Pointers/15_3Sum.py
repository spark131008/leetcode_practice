from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while(left < right):
                sum = n + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    # right -= 1
                    while(nums[left-1] == nums[left] and left < right):
                        left += 1
        return res