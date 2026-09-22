
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count = {}
        for n in nums: 
            count[n] = 1 + count.get(n,0)

        # make heap (priority, num)
        heap = []
        for n in count.keys():
            heapq.heappush(heap, (count[n],n))

            if len(heap) > k:
                heapq.heappop(heap)
        
        # populate res array 
        # (heapq.heappush(heap, item))
        # (heapq.heappop(heap, item))
        # 
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res 