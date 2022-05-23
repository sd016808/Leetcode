#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class Slot:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.BucketSize = 1000
        self.Buckets = [[] for _ in range(self.BucketSize)]

    def put(self, key: int, value: int) -> None:
        bucket = self._getBucket(key)
        for slot in bucket:
            if slot.key == key:
                slot.value = value
                return
        
        bucket.append(Slot(key, value))

    def get(self, key: int) -> int:
        bucket = self._getBucket(key)
        return next((slot.value for slot in bucket if slot.key == key), -1)

    def remove(self, key: int) -> None:
        bucket = self._getBucket(key)
        for i, slot in enumerate(bucket):
            if slot.key == key:
                del bucket[i]
                return
    
    def _getBucket(self, key):
        return self.Buckets[key % self.BucketSize]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

