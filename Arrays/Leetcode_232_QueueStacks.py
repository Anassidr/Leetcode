# naive approach :

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s1.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())
        
    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]
        
    def empty(self) -> bool:
        return self.s1 == []
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue():
    def __init__(self):
        self.in_stk = []
        self.out_stk = []
    def push(self, x):
        self.in_stk.append(x)
    def pop(self):
        self.peek()
        return self.out_stk.pop()
    def peek(self):
        # as long as the out stack is not empty, we will keep popping from it because it has the first elements in the queue
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]
    def empty(self):
        return not self.in_stk and not self.out_stk
        