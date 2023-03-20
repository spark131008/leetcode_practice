class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store tuple(temp, index)
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

    def dailyTemperatures_2(self, temperatures: List[int]) -> List[int]:
        stack = [] # Store index of each day's temperature
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append(i)
        return res

    def dailyTemperatures_2(self, temperatures: List[int]) -> List[int]:
        hottest = 0
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            if temperatures[i] > hottest:
                hottest = temperatures[i]
                continue

            days = 1
            while temperatures[i + days] < temperatures[i]:
                print(temperatures[i])
                days += 1
            res[i] = days
        return res



















    