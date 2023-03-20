from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        sqaure_hash = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue

                if board[row][col] in row_hash[row]:
                    return False

                if board[row][col] in col_hash[col]:
                    return False

                if board[row][col] in sqaure_hash[(row // 3, col // 3)]:
                    return False

                row_hash[row].add(board[row][col])
                col_hash[col].add(board[row][col])
                sqaure_hash[(row // 3, col // 3)].add(board[row][col])
        return True