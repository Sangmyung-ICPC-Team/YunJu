from itertools import combinations
from unittest import result

L , C = map(int,input().split())
li = list(map(str,input().split()))

li.sort()
answer = []

def dfs(count):
    first = 0
    second = 0
    for i in range(len(count)):
        if count[i] == 'a':
            first += 1
        elif count[i] == 'i':
            first += 1
        elif count[i] == 'e':
            first += 1
        elif count[i] == 'o':
            first += 1
        elif count[i] == 'u':
            first += 1
        else:
            second += 1
    if first >= 1 and second >=2 :
        return True
    else:
        return False

for count in combinations(li, L):
    if dfs(count):
        answer.append(count)

for ans in answer:
    result = ''
    for i in ans:
        result += str(i)
    print(result)
