class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def partition(nums, start, end):
            pivot = (start + end) // 2
            tmp = nums[pivot]
            nums[pivot] = nums[end]
            nums[end] = tmp
            
            for i in range(start, end):
                if nums[i] < nums[end]:
                    tmp = nums[start]
                    nums[start] = nums[i]
                    nums[i] = tmp
                    start += 1
                    
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            return start
			
        def quicksort(nums, start, end):
            if start >= end:
                return
            pivot = partition(nums, start, end)
            quicksort(nums, start, pivot-1)
            quicksort(nums, pivot+1, end)
			
        quicksort(nums, start = 0, end = len(nums)-1)
        return nums