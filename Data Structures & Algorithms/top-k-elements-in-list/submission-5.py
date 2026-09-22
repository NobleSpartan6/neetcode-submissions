class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count = {}

        # freq of nums { n : freq}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # create heap
        heap = []

        # loop through nums by accessing the keys
        for n in count.keys():
            # push item (count[n], n)
            # Example nums = [1,2,2,3,3,3], k = 2
            # count = {1:1,2:2,3:3}
            # n = 1, item = (count[1], 1) = (1,1)
            # why are we pushing items on the heap like this?
            heapq.heappush(heap, (count[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

