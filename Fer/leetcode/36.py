class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row
        for i in board:
            c = set()
            for j in i:
                if j not in c:
                    c.add(j)
                else:
                    return False
        #check columns
        for i in range(9):
            c = set()
            for j in board:
                if j[1] not in c:
                    c.add(j[1])
                else:
                    return False
        #check subbboxes
        for i in range(3):
            for j in range(3):
                