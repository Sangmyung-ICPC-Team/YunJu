n = int(input())

P = [1,1,1,2,2]

for i in range(5, 100):
    P.append(P[i-1] + P[i-5])

for _ in range(n):
    N = int(input())
    print(P[N-1])