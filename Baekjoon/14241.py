N = int(input())
slime = list(map(int, input().split())) 
slime.sort(reverse = True)

sum, score, result = 0, 0, 0 

for i in range(0, N - 1): 
    score = slime[i] * slime[i+1] 
    slime[i+1] = slime[i] + slime[i+1] 
    result = result + score     
    
print(result)
