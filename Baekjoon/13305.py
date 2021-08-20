import sys

N = int(input())
M = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

sum = 0
first = price[0]

for i in range(len(M)):
    if price[i] < first:
        first = price[i]
    sum += M[i] * first

print(sum)