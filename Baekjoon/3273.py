import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
li.sort()

x = int(input())
count = 0
start = 0
end = n - 1

while start != end:
    if li[start] + li[end] == x:
        count += 1
        start += 1
    elif li[start] + li[end] > x:
        end -= 1
    else:
        start += 1

print(count)