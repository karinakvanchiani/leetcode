class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if i < len(nums1):
            merged.extend(nums1[i:])

        if j < len(nums2):
            merged.extend(nums2[j:])

        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2] + merged[n // 2 - 1]) / 2
        else:
            return float(merged[n // 2])