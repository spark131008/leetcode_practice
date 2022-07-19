from typing import *
from collections import deque

class Solution:
    def children(self, lock):
        res = []
        for i in range(len(lock)):
            i_up = str((int(lock[i])+1) % 10)
            comb1 = lock[:i] + i_up + lock[i+1:]
            res.append(comb1)
            i_down = str((int(lock[i])-1+10) % 10)
            comb2 = lock[:i] + i_down + lock[i+1:]
            res.append(comb2)
        return res

    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        # 1. if 0000 in deadend - return -1
        # 2. use BFS for minimum turn
        # 3. use a tuple format as lock, turn to count turns to get the solution lock
        # 4. use a hashset to avoid any duplicate visit of a lock
        # 5. use a queue to check each lock combo

        my_queue = deque()
        my_queue.append(["0000", 0])
        visit = set(deadends)

        print(my_queue)
        print(visit)

        while my_queue:
            lock, turn = my_queue.popleft()
            if lock == target:
                return turn
            for child in self.children(lock):
                if child not in visit:
                    visit.add(child)
                    my_queue.append([child, turn+1])
        return -1