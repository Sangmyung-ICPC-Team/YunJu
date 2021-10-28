n = int(input())

xlist = list(map(int, input().split()))

anslist = sorted(list(set(xlist)))

dic = {anslist[i] : i for i in range (len(anslist))}

for i in xlist:
    print(dic[i], end = ' ')