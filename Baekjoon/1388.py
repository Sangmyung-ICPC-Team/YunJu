N, M = map(int, input().split())
answer, check1, check2 = 0, 0, 0
li = [input() for i in range(N)]

visit = [[0 for i in range(N)] for j in range(M)]

for i in range(N):
    for j in range(M):
        if li[i][j] == '-':
            check1 = 1
        elif li[i][j] == '|' and check1 > 0:
            answer += 1
            check1 = 0
    if check1 > 0:
        answer += 1
        check1 = 0

for i in range(M):
    for j in range(N):
        if li[j][i] == '|':
            check2 = 1
        elif li[j][i] == '-' and check2 > 0:
            answer += 1
            check2 = 0
    if check2 > 0:
        answer += 1
        check2 = 0

print(answer)