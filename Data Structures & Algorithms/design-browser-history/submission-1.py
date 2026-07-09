class HistoryButtons:
    def __init__(self, page = ""):
        self.page = page
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        # Create sentinel head and tail
        self.head = HistoryButtons()
        self.tail = HistoryButtons()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        self.currPage = self.head  # Initialize currPage to head
        self.visit(homepage)  # Visit homepage

    def visit(self, url: str) -> None:
        # Remove nodes between currPage and tail (clear forward history)
        self.currPage.next = self.tail
        self.tail.prev = self.currPage
        # Create a new node and link it to the current node
        newPage = HistoryButtons(url)
        newPage.prev = self.currPage
        newPage.next = self.tail
        self.currPage.next = newPage
        self.tail.prev = newPage
        # Update what the current page is
        self.currPage = newPage

    def back(self, steps: int) -> str:
        # Move back in history
        while steps > 0 and self.currPage.prev != self.head:
            self.currPage = self.currPage.prev
            steps -= 1
        return self.currPage.page

    def forward(self, steps: int) -> str:
        # Move forward in history
        while steps > 0 and self.currPage.next != self.tail:
            self.currPage = self.currPage.next
            steps -= 1
        return self.currPage.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)