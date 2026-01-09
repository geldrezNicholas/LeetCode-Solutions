class BrowserHistory:

    def __init__(self, homepage: str):
        self.backS = [homepage]
        self.forwardS = []

    def visit(self, url: str) -> None:
        self.forwardS = []
        self.backS.append(url)

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.backS) > 1:
            curr = self.backS.pop()
            self.forwardS.append(curr)
            steps-=1
        return self.backS[-1]

    def forward(self, steps: int) -> str:
            while steps > 0 and len(self.forwardS) > 0:
                nextpg = self.forwardS.pop()
                self.backS.append(nextpg)
                steps-=1
            return self.backS[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)