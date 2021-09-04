import sys

def num(n, k, test):
    tmp = sum(test[:k])
    answer = tmp

    for i in range(k,n):
        tmp += test[i]
        tmp -= test[i-k]
        if tmp > answer:
            answer = tmp
    return answer if n != k else tmp

n, k = map(int,sys.stdin.readline().split())
test = list(map(int,sys.stdin.readline().split()))

print(num(n, k, test))