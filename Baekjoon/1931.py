num = int(input())
arr = []

for i in range(num):
    one, two = map(int, input().split())
    j.append([one, two])

j = sorted(j, key=lambda a: a[0])
j = sorted(j, key=lambda a: a[1])

last = 0
count = 0

for i, k in j:
    if i >= last:
        count += 1
        last = k

print(count)
