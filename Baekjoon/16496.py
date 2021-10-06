import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(str, input().split()))
        
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
print(answer)
        