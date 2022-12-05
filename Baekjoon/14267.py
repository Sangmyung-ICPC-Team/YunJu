import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

node = [[] for i in range(n+1)] 
clist = [0 for i in range(n+1)]

people = list(map(int, input().split()))

def dfs(num, size):
    for i in node[num]:
        if(num < i):
            clist[i] += size
            dfs(i, size)

for i in range(1, n+1) :
    node[i].append(people[i-1])
    if(people[i-1] != -1): 
        node[people[i-1]].append(i)

for j in range(m): 
    i, w = map(int, input().split())
    clist[i] += w 
    dfs(i, w)
  
for i in clist[1::]:
    print(i, end=" ")