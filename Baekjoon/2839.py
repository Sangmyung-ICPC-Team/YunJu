N = int(input())

sugar = 0

while True:
    if (N % 5) == 0:
        sugar = sugar + (N//5)
        print(sugar)
        break
    N = N - 3
    sugar += 1

    if N < 0:
        print("-1")
        break
