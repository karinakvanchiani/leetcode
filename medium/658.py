class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = []
        closest_index, min_diff = 0, abs(x - arr[0])

        for i in range(len(arr)):
            diff = abs(x - arr[i])
            diffs.append(diff)

            if diff < min_diff:
                closest_index, min_diff = i, diff

        if k == 1:
            return [arr[closest_index]]

        l, r = closest_index - 1, closest_index + 1

        while l >= 0 and r < len(arr) and r - l < k:
            if diffs[l] <= diffs[r]:
                l -= 1
            else:
                r += 1

        if l < 0:
            return arr[:k]
        
        if r >= len(arr):
            return arr[-k:]

        if r - l == k:
            if diffs[l] <= diffs[r]:
                return arr[l:r]
            else:
                return arr[l + 1:r + 1]
            
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diffs = {}

        for i in range(len(arr)):
            diff = abs(x - arr[i])

            if diff not in diffs:
                diffs[diff] = []
            diffs[diff].append(arr[i])

        result = []

        sorted_keys = sorted(list(diffs.keys()))
        for key in sorted_keys:
            if len(result) == k:
                break

            result += diffs[key][:k - len(result)]

        return sorted(result)