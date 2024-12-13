class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        merged = intervals[0]
        merged_intervals = []

        for interval in intervals[1:]:
            if interval[0] <= merged[1]:
                merged[1] = max(merged[1], interval[1])

            else:
                merged_intervals.append(merged)
                merged = interval

        merged_intervals.append(merged)
        return merged_intervals