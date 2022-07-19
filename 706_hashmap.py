class myHashMap():
    def __init__(self):
        self._v = [-1]*1000001

    def put(self, key, value):
        self._v[key] = value

    def get(self, key):
        return self._v[key]

    def remove(self, key):
        self._v[key] = -1


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