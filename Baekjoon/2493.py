import sys
input = sys.stdin.readline

n = int(input()) 

tap = list(map(int,input().split()))

stack = []
ans = []

for i in range(n):
    while stack:
        if stack[1] >= tap[i]: 
            ans.append(stack[0] + 1)
            break
        
        else: stack.pop()

    if not stack:
        ans.append(0) 
    
    stack.append((i, tap[i]))

for i in ans:
    print(i, end = ' ')