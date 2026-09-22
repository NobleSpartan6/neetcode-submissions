class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        # hashmap { key : number , value : count }
        freq = {}

        for n in nums: 
            freq[n] = 1 + freq.get(n,0)
        
        # EXAMPLE 1: [1,2,2,3,3,3]
        # freq = {1:1, 2:2, 3:3}
        heap = []
        # 
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            # keep pushing elements on the heap then pop when we hit the limit
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res