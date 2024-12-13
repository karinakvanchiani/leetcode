class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        intrsct = []

        count1 = Counter(nums1)
        count2 = Counter(nums2)

        for k, v in count1.items():
            if k in count2:
                intrsct.extend([k] * min(v, count2[k]))

        return intrsct