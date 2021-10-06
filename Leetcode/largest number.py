class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        
        def b_sort(nums):
            for i in range(len(nums)):
                for j in range(len(nums) - 1):
                    if (nums[j] + nums[j+1]) < (nums[j+1] + nums[j]):
                        tmp = nums[j+1]
                        nums[j+1] = nums[j]
                        nums[j] = tmp
            return nums
        
        b_sort(nums)
        answer = ''.join(nums)
        
        if nums.count('0') == len(nums):
            answer = '0'
        return answer
        