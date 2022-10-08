class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1
            return hours <= h

        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if canEatAllBananas(mid):
                right = mid
            else:
                left = mid + 1
        return left
