n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
miv = 100000001
mav = -100000001

def dfs(i, li):
    global add, sub, mul, div, miv, mav
    if(i == n):
        mav = max(mav, li)
        miv = min(miv, li)
    if(add > 0):
        add -= 1
        dfs(i+1, li + num[i])
        add += 1
    if(sub > 0):
        sub -= 1
        dfs(i+1, li - num[i])
        sub += 1
    if(mul > 0):
        mul -= 1
        dfs(i+1, li * num[i])
        mul += 1
    if(div > 0):
        div -= 1
        dfs(i+1, int(li / num[i]))
        div += 1

dfs(1, num[0])
print(mav)
print(miv)