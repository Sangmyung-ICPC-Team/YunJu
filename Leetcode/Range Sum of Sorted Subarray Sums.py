class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        li = [nums[0]]
        
        for i in range(1, n):
            li.append(nums[i])    
            nums[i] += nums[i-1]
            li.append(nums[i]) 
            
            for j in range(i-1):
                li.append(nums[i] - nums[j])
                
        li.sort()       
        
        return sum(li[left-1:right]) % 1000000007