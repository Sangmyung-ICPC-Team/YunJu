class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def visit(i, j, words, alp):
            if words == word:
                return True
            
            for a, b in [(-1,0), (0,-1), (1,0), (0,1)]:
                rx = i + a
                ry = j + b
                
                if rx < 0 or ry < 0 or rx >= len(board) or ry >= len(board[0]) or (rx, ry) in li:
                    continue
                else:
                     if board[rx][ry] == word[alp]:
                        li.append((rx, ry))
                        if visit(rx, ry, words + board[rx][ry], alp + 1):
                            return True
                        else:
                            li.pop()
                            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    li = []
                    li.append((i, j))
                    answer = visit(i, j, word[0], 1)

                    if answer:
                        return True
        return False
        