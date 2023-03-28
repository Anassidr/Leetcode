# problem 1656 Design an Ordered Stream

class OrderedStream:

    def __init__(self, n: int):
        self.map = {}
        self.i = 1
        

    def insert(self, idKey: int, value: str) -> list[str]:
        self.map[idKey] = value
        chunk = []
        while self.i in self.map:
            chunk.append(self.map[self.i])
            self.i += 1
        return chunk
    