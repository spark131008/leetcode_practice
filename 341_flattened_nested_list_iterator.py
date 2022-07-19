from collections import deque

# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque(nestedList)

    def next(self) -> int:
        return self.queue.popleft().getInteger()

    def hasNext(self) -> bool:
        while self.queue:
            if self.queue[0].isInteger():
                return True
            else:
                poppedList = self.queue.popleft().getList()
                for i in poppedList[::-1]:
                    self.queue.appendleft(i)
        return False