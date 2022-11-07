class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)
        self.w = [w[0]]
        for i in range(1, len(w)):
            self.w.append(self.w[-1] + w[i])


    def pickIndex(self) -> int:
        r = random.randint(1, self.total)
        return bisect.bisect_left(self.w, r)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()