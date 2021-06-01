import sys

num = int(input())

for _ in range(num):
    num = int(input())
    arr = sorted([list(map(int, sys.stdin.readline().strip().split())) for j in range(num)],
                 key = lambda j: j[0])

    count = 1
    min = arr[0][1]

    for i in range(1, num):
        if arr[i][1] < min:
            min = arr[i][1]
            count += 1

    print(count)
    
