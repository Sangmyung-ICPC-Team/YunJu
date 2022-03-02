N, L = map(int,input().split())
li = list(map(int,input().split()))

li.sort()

stop = 1
start = li[0]
end = start + L - 0.5

for i in li:
    if end >= i:
        continue
    else:
        stop += 1
        end = i + L - 0.5

print(stop)