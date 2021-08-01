num = int(input())

for _ in range(num):
    count = 0
    arr = list(map(int, input().split()))
    avg = (sum(arr)-arr[0])/arr[0] 
    
    for i in arr[1:]:
        if i > avg:
            count+=1
    r = count/arr[0]*100

    print(f"{r:.3f}%")