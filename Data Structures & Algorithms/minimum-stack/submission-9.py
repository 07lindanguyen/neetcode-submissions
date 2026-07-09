class MinStack:
    # design like an array
    # use mutables like append and remove
    # each time you add and pop and item
    # you should record the minimum
    # NEW VALUES WITH CURRENT MINIMUM
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if not empty
        # compare current min with added in val
        if self.minStack:
            val = min(val, self.minStack[-1])
        else:
            val = val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        # pop from min_stack because pushed values
        # are tethered to min values
        # so get rid of both
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
