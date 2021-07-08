n = int(input())
cnt = 0
li = [0,0,1,1]

for i in range(4, n+1):

    li.append(li[i-1] + 1)
    
    if i % 2 == 0:
        li[i] = min(li[i//2] + 1, li[i])
    if i % 3 == 0:
        li[i] = min(li[i//3] + 1, li[i])
        
print(li[n])