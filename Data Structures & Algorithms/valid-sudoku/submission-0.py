class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)  # key = (r//3 , c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if ((board[r][c] in row[r]) or 
                    (board[r][c] in col[c]) or 
                    (board[r][c] in box[(r//3 , c//3)])):
                    return False

                row[r].add(board[r][c])
                col[c].add(board[r][c])
                box[(r//3, c//3)].add(board[r][c])  # 0,1,2 -> 0; 3,4,5 -> 1; 6,7,8 -> 2

        return True