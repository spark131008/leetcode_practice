class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = [-1] * k
        self.head = self.tail = -1

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = self.tail = 0
            self.queue[self.head] = value
            return True
        else:
            self.head = (self.head + self.k - 1) % self.k
            self.queue[self.head] = value
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = self.tail = 0
            self.queue[self.head] = value
            return True
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head = self.tail = -1
            return True
        else:
            self.head = (self.head + 1) % self.k
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head = self.tail = -1
            return True
        else:
            self.tail = (self.tail + self.k - 1) % self.k
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head == -1 or self.tail == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.tail + 1) % self.k == self.head:
            return True
        else:
            return False
