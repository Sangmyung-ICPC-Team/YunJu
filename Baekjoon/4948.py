import math 

while True: 
    n = int(input()) 

    if n == 0: 
        break

    count = 0 
    answer = [True]* (2 * n + 1)  
    
    for i in range(2, int(math.sqrt(2*n) + 1)): 
        if answer[i]: 
            j = 2

            while i * j <= 2*n: 
                answer[i*j] = False 
                j += 1 
            
    for x in range(n+1, 2*n +1): 
        if answer[x]: 
            count += 1 
    print(count)
