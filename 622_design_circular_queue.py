class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.k = k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        elif self.isEmpty():
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = value
            return True

        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        else:
            self.head = (self.head + 1) % self.k
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            print(self.head)
            return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return True if self.head == -1 else False

    def isFull(self) -> bool:
        return True if (self.tail + 1) % self.k == self.head else False