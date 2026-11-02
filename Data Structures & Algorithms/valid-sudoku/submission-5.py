class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use row 、 col 、sub-box set to prevent repeat number
        row = defaultdict(set)
        col = defaultdict(set)
        subBox = defaultdict(set)

        for r in range(len(board)):
          for c in range(len(board)):
            val = board[r][c]
            if val == '.':
              continue
            if val in row[r] or val in col[c] or val in subBox[(r//3, c//3)]:
              return False
            row[r].add(val)
            col[c].add(val)
            subBox[(r//3, c//3)].add(val)
        return True