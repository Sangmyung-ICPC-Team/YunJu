import sys
N = int(sys.stdin.readline().strip())
num = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
find_list = list(map(int, sys.stdin.readline().split()))

for i in find_list:
    if i in num:
        print(1)
    else:
        print(0)