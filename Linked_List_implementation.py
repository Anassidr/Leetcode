class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def countNodes(self, node):
        if node:
            self.count += 1
            return self.countNodes(node.next)
        return self.count

node_a = Node(5)
node_b = Node(3)
node_a.next = node_b

mylist = LinkedList()
mylist.head = node_a 

# print(mylist.countNodes(node_a))

print(int("101", 2))
