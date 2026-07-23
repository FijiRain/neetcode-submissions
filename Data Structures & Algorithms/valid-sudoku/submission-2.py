class Solution:
    def check_lines(self, row: List[str]) -> bool:
        visited = []
        for i in row:
            if i in visited:
                return False
            if i != ".":
                visited.append(i)
        return True

    def check_col(self, board: List[List[str]], index: int) -> bool:
        visited = []
        for row in board:
            if row[index] in visited:
                return False
            if row[index] != ".":
                visited.append(row[index])
        return True

    def check_boxes(self, board: List[List[str]]) -> bool:
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                visited = []

                for row in range(3):
                    for col in range(3):
                        value = board[start_row + row][start_col + col]

                        if value in visited:
                            return False
                        if value != ".":
                            visited.append(value)
        return True



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check_lines(row):
                return False
        for index in range(len(board[0])):
            if not self.check_col(board, index):
                return False 
        if not self.check_boxes(board):
            return False
        return True
        