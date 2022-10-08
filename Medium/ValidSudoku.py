class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            if not self.is_valid(row):
                return False
        # Check columns
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if not self.is_valid(column):
                return False
        # Check boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for k in range(3):
                    for l in range(3):
                        box.append(board[i + k][j + l])
                if not self.is_valid(box):
                    return False
        return True

    def is_valid(self, box):
        box = [x for x in box if x != '.']
        return len(box) == len(set(box))
