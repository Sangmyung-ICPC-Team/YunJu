K = int(input())
B = input().split()

visit = [0] * 10
max = ""
min = ""

def check(i, j, k):
    if k == '>':
        return i > j
    else:
        return i < j

def backtracking(n, m):
    global max, min

    if(n == K+1):
        if(len(min) == 0):
            min = m
        else:
            max = m
        return
    
    for i in range(10):
        if(visit[i] == 0):
            if(n == 0 or check(m[-1], str(i), B[n-1])):
                visit[i] = True
                backtracking(n + 1, m + str(i))
                visit[i] = False

backtracking(0, "")
print(max)
print(min)
