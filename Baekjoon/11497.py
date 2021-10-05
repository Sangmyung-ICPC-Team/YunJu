T = int(input())

for _ in range(T):
    test = []
    n = int(input())
    test = list(map(int, input().split()))

    test.sort() 
    max = 0 
    
    for i in range(len(test) - 2): 
        if (test[i + 2] - test[i] > max): 
            max = test[i + 2] - test[i] 
    
    print(max)
