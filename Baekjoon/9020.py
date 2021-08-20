def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n/2) + 2):
            if (n % i == 0):
                return False
        return True


answer = []
n = int(input())
m = []

for i in range(0, n):
    m.append(int(input()))
    answer.append(0)

for i in range(0, n):
    tmp = int(m[i] / 2)
    for j in range(tmp, 0, -1):
        if isprime(j):
            if isprime(m[i] - j):
                answer[i] = j
                break

for i in range(0, n):
    print(answer[i], m[i] - answer[i])