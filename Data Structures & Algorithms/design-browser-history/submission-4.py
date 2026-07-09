class HistoryButtons:
    #nodes are the url's (value) you've been to/ are curr at
    def __init__(self, page = ""):
        self.page = page
        self.next = None
        self.prev = None

class BrowserHistory:
    # <>: to go back and forth btwn urls; exceptionally akin to a DLL structure
    # homepage is a node
    def __init__(self, homepage: str):
        self.currPage = HistoryButtons(homepage)

    def visit(self, url: str) -> None:
        # clear forward history
        self.currPage.next = None
        # Create a new node and link it to the current node
        newPage = HistoryButtons(url)
        newPage.prev = self.currPage
        self.currPage.next = newPage
        # Update what the current page is
        self.currPage = newPage

    def back(self, steps: int) -> str:
        # Move back in history
        while steps > 0 and self.currPage.prev is not None:
            self.currPage = self.currPage.prev
            steps -= 1
        return self.currPage.page

    def forward(self, steps: int) -> str:
        # Move forward in history
        while steps > 0 and self.currPage.next is not None:
            self.currPage = self.currPage.next
            steps -= 1
        return self.currPage.page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)