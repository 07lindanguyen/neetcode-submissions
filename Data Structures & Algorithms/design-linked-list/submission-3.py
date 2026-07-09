class MyDLLNode:
    # the node attributes; insert default values in parameters
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    # structure of a list
    def __init__(self):
        # dummy head and tails to have something to connect to
        self.head = MyDLLNode()
        self.tail = MyDLLNode()
        # connect the tail and head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
        return curr.val
    
    def addAtHead(self, val: int) -> None:
        curr = self.head
        NewNode = MyDLLNode(val)
        AfterNew = curr.next
        curr.next = NewNode
        NewNode.next = AfterNew
        AfterNew.prev = NewNode
        NewNode.prev = curr
        self.size += 1
    
    def addAtTail(self, val: int) -> None:
        last = self.tail
        NewNode = MyDLLNode(val)
        beforeNew = last.prev
        last.prev = NewNode
        NewNode.next = last
        beforeNew.next = NewNode
        NewNode.prev = beforeNew      
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        #stop just before the given index for SLL
        if index < 0:
            index = 0
        if index == self.size:
            self.addAtTail(val)
            return
        if index > self.size:
            return None
        curr = self.head
        for i in range(index):
            curr = curr.next
        NewNode = MyDLLNode(val)        
        AfterNew = curr.next
        curr.next = NewNode
        NewNode.prev = curr
        NewNode.next = AfterNew
        AfterNew.prev = NewNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
        AfterOld = curr.next
        BeforeOld = curr.prev
        BeforeOld.next = AfterOld
        AfterOld.prev = BeforeOld
        self.size -= 1
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)