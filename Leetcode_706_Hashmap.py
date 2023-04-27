class MyHashMap:

    def hash_eval(self, key):
        return ((key*1031237) & (1<<20) - 1) >> 5 

    def __init__(self):
        self.myHashMap = [{} for _ in range(1<<15)]

    def put(self, key: int, value: int) -> None:
        spot = self.hash_eval(key)
        self.myHashMap[spot][key] = value

    def get(self, key: int) -> int:
        spot = self.hash_eval(key)
        if key in self.myHashMap[spot]:
            return self.myHashMap[spot][key]
        else:
            return -1 

    def remove(self, key: int) -> None:
        spot = self.hash_eval(key)
        if key in self.myHashMap[spot]:
            del self.myHashMap[spot][key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)