def prime(n):
    i = 2
    if n == 1:
        return False

    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n, m = map(int, input().split())
for i in range(n, m+1):
    if(prime(i)):
        print(i)