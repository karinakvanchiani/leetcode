class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        if len(heights) == 1:
            return [0]

        visible = [0]
        stack = [heights[-1]]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[i + 1]:
                if heights[i] > stack[0]:
                    visible.append(len(stack))
                    stack = [heights[i]]

                else:
                    for k in range(len(stack) - 1, -1, -1):

                        if stack[k] > heights[i]:
                            visible.append(len(stack[k:]))
                            stack = stack[:k + 1]
                            break

                    stack.append(heights[i])
            else:
                visible.append(1)
                stack.append(heights[i])

        return visible[::-1]