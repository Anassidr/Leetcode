class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.myHashMap = [None for _ in range(1<<15)]

    def hash_eval(self, key):
        return ((key*1031237) & (1<<20) - 1) >> 5 

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        index = self.hash_eval(key)
        node = self.myHashMap[index]
        new_node = ListNode(key, value)
        new_node.next = node
        self.myHashMap[index] = new_node
        return


    def get(self, key: int) -> int:
        index = self.hash_eval(key)
        node = self.myHashMap[index]
        if node == None:
            return -1
        else:
            while node:
                if node.key == key:
                    return node.val
                node = node.next
            return -1

    def remove(self, key: int) -> None:
        index = self.hash_eval(key)
        node = self.myHashMap[index]
        if node != None:
            if node.key == key:
                self.myHashMap[index] = node.next
            else:
                while node and node.next:
                    if node.next.key == key:
                        if node.next.next:
                            node.next = node.next.next
                        else:
                            node.next = None
                        return 
                    node = node.next
                


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)