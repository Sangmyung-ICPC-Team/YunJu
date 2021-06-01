arr = []
num = int(input())
arr = list(map(int, str(num)))
arr.sort(reverse = True)

for num in arr :
    print(num, end="")
