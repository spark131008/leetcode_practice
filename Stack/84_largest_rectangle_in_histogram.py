from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                stack_i, stack_h = stack.pop()
                start = stack_i
                area = (index - stack_i) * stack_h
                largest = max(largest, area)
            stack.append((start, height))

        for index, height in stack:
            area = (len(heights) - index) * height
            largest = max(largest, area)
        return largest
