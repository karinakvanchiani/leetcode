class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            n = len(nums)

            if n <= 1:
                return nums

            mid_idx = n // 2
            left_part = nums[:mid_idx]
            right_part = nums[mid_idx:]

            merge_sort(left_part)
            merge_sort(right_part)

            merge(left_part, right_part, nums)

        def merge(arr1, arr2, source_array):
            p1, p2, n1, n2 = 0, 0, len(arr1), len(arr2)
            write_ind = 0

            while p1 < n1 or p2 < n2:
                if p1 == n1 or (p2 != n2 and arr2[p2] < arr1[p1]):
                    source_array[write_ind] = arr2[p2]
                    p2 += 1

                elif p2 == n2 or (p1 != n1 and arr1[p1] <= arr2[p2]):
                    source_array[write_ind] = arr1[p1]
                    p1 += 1

                write_ind += 1

        merge_sort(nums)
        return nums