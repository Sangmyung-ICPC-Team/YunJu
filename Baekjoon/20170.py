import fractions

n = list(input().split())
m = list(input().split())
win = 0

for i in range(6):
    for j in range(6):
        if(n[i] > m[j]):
            win += 1

ans = fractions.Fraction(win, 36)
U = ans.numerator
D = ans.denominator

print("%d/%d" %(U, D))

