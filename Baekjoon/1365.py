import sys

def lower_bound(s, e, v):
    while s < e:
        m = (s + e) // 2
        if ans[m] < v:
            s = m + 1
        else:
            e = m
    return e

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
ans = []

for i in range(n):
    if i == 0:  
        ans.append(li[0])
    if ans[-1] < li[i]:   
        ans.append(li[i])
    else:  
        tmp = lower_bound(0, len(ans), li[i])
        ans[tmp] = li[i]


print(n - len(ans))