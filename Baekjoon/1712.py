A, B, C = map(int, input().split())

if (C - B) <= 0:
    print("-1")
    
else:
    n = A / (C - B)
    n = n + 1
    print(int(n))