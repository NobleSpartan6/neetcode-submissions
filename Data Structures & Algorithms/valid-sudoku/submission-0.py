class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we are scanning through the rows, cols, and boxes and checking for dups
        # rows[9] - each entry is a set of digits seen in that row
        # cols[9] - each entry is a set of digits seen in that col 
        # squares[9] - each entry is a set of digits seen in that 3x3 box
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # loop through matrix
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # index into each dict first:
                if (board[r][c] in rows[r] or
                 board[r][c] in cols[c] or
                  board[r][c] in squares[(r//3, c//3)]):
                    return False
                # add the value to the set (do not assign)
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                # we are indexing the 3x3 box and storing as a tuple key
                squares[(r//3,c//3)].add(board[r][c])
        
        return True