import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        groups = {}

        for i in range(0, 81): 
            r = i // 9
            c = i % 9

            if board[r][c] != ".":
                # groups[f"{r}"] = groups.get(f"{r}", []).append(board[r][c])
                # groups[f"{c}"] = groups.get(f"{c}", []).append(board[r][c])

                if f"r{r}" not in groups:
                    groups[f"r{r}"] = []
                    groups[f"r{r}"].append(board[r][c])
                else:
                    groups[f"r{r}"].append(board[r][c])

                if f"c{c}" not in groups:
                    groups[f"c{c}"] = []
                    groups[f"c{c}"].append(board[r][c])
                else:
                    groups[f"c{c}"].append(board[r][c])
                
                s = (r // 3) * 3 + (c // 3)
                
        
                groups.setdefault(f"s{s}", []).append(board[r][c])
                
                # if f"s{s}" not in groups:
                #     groups[f"s{s}"] = []
                #     groups[f"s{s}"].append(board[r][c])
                # else:
                #     groups[f"s{s}"].append(board[r][c])
        
        for j in list(groups.values()):
            if len(set(j)) != len(j):
                print(j)
                return False
        return True