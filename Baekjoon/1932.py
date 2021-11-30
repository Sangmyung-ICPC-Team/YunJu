n = int(input())
li = []

for _ in range(n):
    li.append(list(map(int, input().rstrip().split())))
    
for i in range(1, n):
    l = len(li[i])
    for j in range(l):
        temp = []
        if (0 <= j - 1):  
            temp.append(li[i - 1][j - 1])
        if (j < l - 1):  
            temp.append(li[i - 1][j])
        li[i][j] += max(temp)

print(max(li[n - 1]))