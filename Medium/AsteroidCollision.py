class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                while stack and 0 < stack[-1] < abs(i):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(i)
                elif stack[-1] == abs(i):
                    stack.pop()
        return stack
