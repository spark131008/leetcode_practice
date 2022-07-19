from collections import deque

class RecentCounter:

    def __init__(self):
        self.callList = deque()

    def ping(self, t: int) -> int:
        self.callList.append(t)
        while self.callList[0] < t - 3000:
            self.callList.popleft()
        return len(self.callList)
