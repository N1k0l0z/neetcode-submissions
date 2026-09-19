import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        groups = {}

        for i in range(0, 81): 
            r = i // 9
            c = i % 9
            s = (r // 3) * 3 + (c // 3)

            if board[r][c] != ".":

                groups.setdefault(f"r{r}", []).append(board[r][c])
                groups.setdefault(f"c{c}", []).append(board[r][c])
                groups.setdefault(f"s{s}", []).append(board[r][c])
        
        for j in list(groups.values()):
            if len(set(j)) != len(j):
                print(j)
                return False
        return True