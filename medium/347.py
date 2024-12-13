class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        result = {}

        for key, value in counts.items():
            if len(result) < k:
                result[key] = value
            else:
                min_counts = min(result.items(), key=lambda x: x[1])
                if value > min_counts[1]:
                    del result[min_counts[0]]
                    result[key] = value

        return result.keys()
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return list(dict(counts).keys())[:k]