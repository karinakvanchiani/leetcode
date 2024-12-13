from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        window = deque()
        slide_maxs = []

        for i in range(len(nums)):
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)

            if i - window[0] == k:
                window.popleft()

            if i + 1 >= k:
                slide_maxs.append(nums[window[0]])

        return slide_maxs