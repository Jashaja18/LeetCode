class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        List = []

        def generate(A='', left=0, right=0):
            if len(A) == 2 * n:
                List.append(A)
                return
            if left < n:
                generate(A + '(', left + 1, right)
            if right < left:
                generate(A + ')', left, right + 1)

        generate()
        return List

        # List = []
        # backtracking = Backtracking
        #     if n == 2:
        #         return n
        #     else:
        #         return [
        #             y + x
        #             for y in self.generateParenthesis(1, n)
        #             for x in self.generateParenthesis(list - 1, n)
        #         ]

# ALGORITHM

# Step 1 − if current_position is goal, return success
# Step 2 − else,
# Step 3 − if current_position is an end point, return failed.
# Step 4 − else, if current_position is not end point, explore and repeat above steps.
