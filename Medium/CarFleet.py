class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]