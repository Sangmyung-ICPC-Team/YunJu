class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        li = []
        nums1 = sorted(nums1)
        nums2 = set(nums2)
            
        for i in nums2:
            start = 0
            end = len(nums1) - 1
            while start <= end:
                mid = (start + end) >> 1
                if nums1[mid] == i:
                    li.append(i)
                    break
                else:
                    if nums1[mid] < i:
                        start = mid + 1
                    else:
                        end = mid - 1
        return li