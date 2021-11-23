w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

px, qy = 1, 1

for i in range(t):
    if(p + px > w or p + px < 0):
        px = -px
    if(q + qy > h or q + qy < 0):
        qy = -qy
    p += px
    q += qy

print(p)
print(q)