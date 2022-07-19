class myHashSet():
    def __init__(self):
        self.numBucket = 10
        self.buckets = [[] for _ in range(self.numBucket)]

    def hashFunc(self, key):
        return key % self.numBucket

    def add(self, key):
        i = self.hashFunc(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self,key):
        i = self.hashFunc(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, key):
        i = self.hashFunc(key)
        if key in self.buckets[i]:
            return True
        return False


# Set is an interface, and HashSet is an implementation of a set.
""" Important Concepts:
    1. Hashing - distributes entries across an array of buckets
               - uses a hash function, a function that passes an entry and generates an index by doing key % (# of buckets)
    2. Collisions - Separate chaining and Open addressing
    3. Load Factor - a critical statistic for a hash table - LF = n/k, 
    where n is # of entries occupied in the hash table
    and where k is # of buckets
      LF must be lower than 0.75
"""