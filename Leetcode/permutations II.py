class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        li = []
        nums.sort()
        
        def dfs(i, nums):            
            if i >= len(nums):
                li.append(nums)
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[i] == nums[j]:
                    continue
                
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1, nums.copy())
                
        dfs(0, nums)
        
        return li