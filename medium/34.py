from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < target:
                l += 1

            if nums[r] > target:
                r -= 1

            if nums[l] == nums[r] == target or nums[l] > target or nums[r] < target:
                break

        if nums[l] == target:
            return [l, r]
        return [-1, -1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(k, l, r):
            position, pivot = -1, -1

            while l < r:
                if pivot == (l + r) // 2:
                    break

                pivot = (l + r) // 2

                if nums[pivot] != target:
                    if 0 <= pivot + k < len(nums) and nums[pivot + k] == target:
                        position = pivot + k
                        break

                if nums[pivot] < target:
                    l = pivot + 1

                elif nums[pivot] > target:
                    r = pivot - 1

                else:
                    if k == 1:
                        r = pivot - 1
                    else:
                        l = pivot + 1
                    position = pivot

            if r - l == 1 and position == -1:
                if nums[r] == target and nums[l] == target:
                    if k == 1:
                        position = l
                    else:
                        position = r
                else:
                    if nums[l] == target:
                        position = l
                    elif nums[r] == target:
                        position = r

            if l == r and nums[l] == target:
                position = l

            return position

        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        pos0 = search(1, 0, len(nums) - 1)
        pos1 = search(-1, max(pos0, 0), len(nums) - 1)

        if pos0 != -1 and pos1 != -1:
            return [pos0, pos1]

        return [max(pos0, pos1), max(pos0, pos1)]