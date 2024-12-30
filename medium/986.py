class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        ans = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            int1, int2 = firstList[i], secondList[j]

            max_start = max(int1[0], int2[0])
            min_end = min(int1[1], int2[1])

            if max_start <= min_end:
                ans.append([max_start, min_end])

            i = i + 1 if int1[1] <= int2[1] else i
            j = j + 1 if int1[1] >= int2[1] else j

        return ans