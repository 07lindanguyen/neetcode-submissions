class MyStack:

    def __init__(self):
        #container
        self.box = []

    def push(self, x: int) -> None:
        self.box.append(x)

    def pop(self) -> int:
        return self.box.pop()
        

    def top(self) -> int:
        return self.box[-1]

    def empty(self) -> bool:
        if self.box == []:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()