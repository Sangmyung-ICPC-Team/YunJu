import sys 

n = int(input()) 
li = [] 
dic = {} 

for i in range(n): 
    i = int(sys.stdin.readline()) 
    li.append(i)

    if i in dic:
        dic[i] += 1 
    else:
        dic[i] = 1

print(round(sum(li)/n)) 

li.sort() 
i = int(len(li)//2) 
print(li[i])


from collections import Counter

k = Counter(li).most_common()

if len(li) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0]) 
    else: 
        print(k[0][0]) 
else: 
    print(li[0])   

print(li[len(li)-1] - li[0])
