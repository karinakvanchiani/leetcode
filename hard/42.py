class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        height_sum = sum(height)
        start = 1 if height[0] > height[1] else 2

        for i in range(start, len(height)):
            if height[i] > height[i - 1]:

                j = i - 2
                while j >= 0 and height[j] <= height[i] and height[j] >= height[j + 1]:
                    j -= 1

                if height[j] < height[j + 1]:
                    j += 1

                j = max(0, j)

                for k in range(j + 1, i):
                    height[k] = min(height[i], height[j])

        return sum(height) - height_sum