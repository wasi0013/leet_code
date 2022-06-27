class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def invalid(row):
            row = [elem for elem in row if elem != "."]
            return len(set(row)) != len(row)
                    
        def check_3x3(board):
            for  r in (0, 3, 6):
                for c in (0, 3, 6):
                    row = [board[i][j] for i in range(r, r+3) for j in range(c, c+3)]
                    if invalid(row):
                        return False
            return True
            
        def is_valid(board):
            for row in board:
                if invalid(row):
                    return False
            for row in zip(*board):
                if invalid(row):
                    return False
            return check_3x3(board)        
        
        return is_valid(board)
            
