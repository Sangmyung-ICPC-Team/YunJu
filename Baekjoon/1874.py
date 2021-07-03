import sys 

n = int(input())
stack = []
answer = []
stacknum = 1


for i in range(n):
    num = int(input())

    while stacknum <= num:
        stack.append(stacknum)
        answer.append('+')
        stacknum += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    
    else:
        print("NO")
        exit(0)

for i in answer:
    print(i)