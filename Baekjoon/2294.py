n, amount = map(int, input().split())

test = [100000 for _ in range(amount + 1)]
test[0] = 0
answer = []
coins = []

for i in range(n):
    coins.append(int(input()))

for i in coins:            
    for j in range(i, amount + 1):  
        test[j] = min(test[j], test[j - i] + 1)     
        answer = test[amount]

if amount == 0:
    print(0)
else:      
    print(answer if test[-1] != 100000 else -1)