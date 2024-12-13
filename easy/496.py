class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for num in nums1:
            num_idx = nums2.index(num)
            added = False

            for i in range(num_idx + 1, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    added = True
                    break
                
            if not added:
                result.append(-1)

        return result