n = int(input())
fi = [0, 1]


for i in range(2, 45):
    fi.append(fi[i-2] + fi[i-1])

for i in range(n):
    num = int(input())
    
    answer = []

    for j in range(len(fi)-1, 0, -1):
        if fi[j] > num:
            continue
        num -= fi[j]
        answer.append(fi[j])
    answer.sort()

    for k in answer:
        print(k, end=' ')
    print()
