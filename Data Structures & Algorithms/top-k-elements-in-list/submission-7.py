class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        heap = []

        for key, value in count.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        
        for value, key in heap:
            res.append(key)

        return res

