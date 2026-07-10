class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1): #stop at last item
        # pop first item then enqueue so the last item is in front
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # push makes the last item added the first item in queue
        return self.q.popleft()

    def top(self) -> int:
        # push makes the last item added the first item in queue
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()