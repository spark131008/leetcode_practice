class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]

        stack = []
        reverseSortedPairs = sorted(pairs)[::-1]
        for p, s in reverseSortedPairs:
            timeToTarget = (target - p) / s
            stack.append(timeToTarget)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)