"""
146. LRU Cache

A cache is a memory that stores date for it
to be served faster in the future.

its purpose is to speed up the data requests

Design and implement a data structure for

Least Recently Used (LRU)

It should support the following operations

get and put

get(key) - get the value (will always be positive) of the key
if the key exists in the cache, otherwise return -1.

put(key,value) set or insert the value if the key is not
already present. When the cache reached its capacity, it 
should invalidate the least recently used item before inserting
a new item.

LRU
Discards the least recently used items first.
The algo requires keeping track of what was used when
which is expensive if one wnats to make sure the algo
always discrads the least recently used item.

General implementations of this technique require
keeping 'age bits' for cache lines and track the
Least Recently Used cache line based on age-bits.

In such an implementation every time a cache line is
used, the age of all other cache lines changes.

LRU is actually a family of caching algorithms with
members includeinig 2Q and LRU/K

The access sequence for the below example is
A B C D E D F

Cache max size is 4 (0,1,2,3)
A(0) B(1)

A(0) B(1) C(2)

A(0) B(1) C(2) D(3)

E(4) B(1) (C2) D(3)

E(4) B(1) C(2) D(5)

E(4) F(6) C(2) D(5)

In the above example once A B C D gets installed 
in the blocks with sequence numbers 
(Increment 1 for each new Access) 

and when E is accessed, it is a miss and it needs to be 
installed in one of the blocks. 


 According to the LRU Algorithm, 
 since A has the lowest Rank(A(0)), 
 E will replace A.


The cache is initialized with a positive capacity.

Follow up:
Could you do both ooperations in O(1) time complexity?

Amazon Microsoft facebook apple bloomberg vmare oracle
bytedance ebay snapchat twilio dropbox google robolx
uber salesforce two sigma intuit telsa asana

https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU

For fast look ups we could use hash map

For fast removal we could use deque
double ended queues

if key is not present return -1
move the key to the front of the queue

"""
from collections import OrderedDict,deque

class LRUCache:
    """
    Shows both the implementation of a double hash or
    with a deque

    LOL MY SOLUTION WAS FASTER

    """

    def __init__(self, capacity: int):
        self.cache = dict()
        self.age_cache = dict()
        self.age_queue = deque()
        self.capacity  = capacity
        self.counter = 0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.age_queue.remove(key)
            self.age_queue.append(key)
            self.age_cache[key] = self.counter
            self.counter+=1
            return self.cache[key]
        else:
            return -1

    def get_2(self, key: int) -> int:
        if key in self.cache:
            self.age_cache[key] = self.counter
            self.counter+=1
            return self.cache[key]
        else:
            return -1
               

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) == self.capacity:
            min_key = min(self.age_cache,key=self.age_cache.get)
            del self.cache[min_key]
            del self.age_cache[min_key]
        self.cache[key] = value
        self.age_cache[key] = self.counter
        self.counter+=1

    def put_2(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.age_queue) == self.capacity:
                min_key = self.age_queue.popleft()
                del self.cache[min_key]
        else:
            self.age_queue.remove(key)
        self.cache[key] = value
        self.age_queue.append(key)
    
    def print_cache(self):
        print(self.counter,self.capacity)
        print(self.cache)
        print(self.age_queue)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    cache.get(1)
    cache.put(3,3)
    cache.print_cache()
    print(cache.get(2))
    cache.put(4,4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

   
    #cache = LRUCache(4)
    # sequence = ['A','B','C','D','E','D','F']
    # for s in sequence:
    #     cache.put(s,0)
    #     cache.print_cache()
    # cache.put(1,1)
    # cache.put(2,2)
    # cache.print_cache()
    # cache.put(3,3)
    # cache.print_cache()
    # cache.put(4,12)
    # cache.print_cache()
    # cache.put(2,2)
    # cache.print_cache()
    # cache.put(2,5)
    # cache.print_cache()
    # print(cache.get(10))
    # print(cache.get(2))
    # LRUCache cache = new LRUCache( 2 /* capacity */ );
    # cache.put(1, 1);
    # cache.put(2, 2);
    # cache.get(1);       // returns 1
    # cache.put(3, 3);    // evicts key 2
    # cache.get(2);       // returns -1 (not found)
    # cache.put(4, 4);    // evicts key 1
    # cache.get(1);       // returns -1 (not found)
    # cache.get(3);       // returns 3
    # cache.get(4);       // returns 4
    
       