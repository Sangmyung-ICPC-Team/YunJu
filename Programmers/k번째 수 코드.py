def solution(array, commands):
    answer = []
    
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
    
    for i in commands:
        cut = array[i[0]-1 : i[1]]
        
        insertion_sort(cut)
             
        answer.append(cut[i[2]-1])    
        
    return answer
