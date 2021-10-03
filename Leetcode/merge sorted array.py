class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j += 1
        
        
        def merge_sort(num):
            if len(num) > 1:
                mid = len(num) // 2
                
                m1 = num[:mid]
                m2 = num[mid:]
                
                merge_sort(m1)
                merge_sort(m2)
                
                i = 0
                j = 0
                k = 0
                
                while i < len(m1) and j < len(m2):
                    if m1[i] < m2[j]:
                        num[k] = m1[i]
                        i += 1
                    else:
                        num[k] = m2[j]
                        j += 1
                    k += 1

                while i < len(m1):
                    num[k] = m1[i]
                    i += 1
                    k += 1

                while j < len(m2):
                    num[k] = m2[j]
                    j += 1
                    k += 1
            return num

            
        return merge_sort(nums1)
        