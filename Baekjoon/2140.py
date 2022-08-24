N = int(input())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):

        if board[i][j] in ('#', '*', 'X'):
            continue

        now = int(board[i][j])
        check = 0
        bomb = 0

        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                check += 1

                if x == 0 and y == 0: 
                    continue

                nx, ny = i + x, j + y

                if 0 <= nx < N and 0 <= ny < N:

                    if board[nx][ny] == '#':
                        if bomb == now:
                            board[nx][ny] = 'X'
                        else:
                            board[nx][ny] = '*'
                            bomb += 1

                    elif board[nx][ny] == '*':
                        bomb += 1
                        
print(sum(int(board[i][j] in ('#', '*')) for i in range(N) for j in range(N)))