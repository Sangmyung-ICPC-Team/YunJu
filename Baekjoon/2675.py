t = int(input())

for i in range(t):
    n, m = input().split()
    n = int(n)
    m = str(m)

    for i in range(len(m)):
        print(n*m[i], end='')
    
    print()