class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # 1. Add x to q2
        self.q2.append(x)
        # 2. Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # 3. Swap q1 and q2
        self.q1 = self.q2
        self.q2 = deque()

    def pop(self) -> int:
        # pop (and return) the front of q1
        return self.q1.popleft()

    def top(self) -> int:
        # peek the front of q1
        return self.q1[0]

    def empty(self) -> bool:
        # check if q1 is empty
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()