class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        ans = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            int1, int2 = firstList[i], secondList[j]

            if int1[0] <= int2[0] <= int1[1] and int1[0] <= int2[1] <= int1[1]:
                ans.append(int2)
            
            elif int2[0] <= int1[0] <= int2[1] and int2[0] <= int1[1] <= int2[1]:
                ans.append(int1)

            elif int1[0] <= int2[0] <= int1[1]:
                ans.append([int2[0], int1[1]])
            
            elif int2[0] <= int1[0] <= int2[1]:
                ans.append([int1[0], int2[1]])

            i = i + 1 if int1[1] <= int2[1] else i
            j = j + 1 if int1[1] >= int2[1] else j

        return ans