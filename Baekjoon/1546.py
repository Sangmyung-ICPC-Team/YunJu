n = int(input())  

test = list(map(int, input().split()))
score = max(test)

M = []
for i in test:
    M.append(i/score * 100) 
result = sum(M)/n

print(result)