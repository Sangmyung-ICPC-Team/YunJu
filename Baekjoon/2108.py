import sys 

n = int(input()) 
arr = [] 
diction = {} 

for _ in range(n): 
    i = int(sys.stdin.readline()) 
    arr.append(i) 
    if i in diction: # 최빈값 계산을 위해 딕셔너리에 담기 
        diction[i] += 1 
    else: diction[i] = 1

print(round(sum(arr)/n)) 

arr.sort() 
i = int(len(arr)//2) 
print(arr[i]) 

maxNum = 0 
arr2 = [] 

for key, val in diction.items(): 
    if val > maxNum: 
        arr2.clear() 
        arr2.append(key) 
        maxNum = val 
    elif val == maxNum: 
        arr2.append(key) 
        maxNum = val 
arr2.sort() 
#print(arr2[0]) 

if len(arr2) == 1:
    print(arr2[0])
else:
    print(arr2[1])  

print(arr[len(arr)-1] - arr[0])
