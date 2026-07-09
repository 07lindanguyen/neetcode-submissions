class MinStack:
    # design like an array
    # use mutables like append and remove

    def __init__(self):
        self.array = []

    def push(self, val: int) -> None:
        self.array.append(val)
        

    def pop(self) -> None:
        if self.array != []:
           self.array.pop()

    def top(self) -> int:
        top = self.array[-1]
        return top

    def getMin(self) -> int:
        return min(self.array)
        
