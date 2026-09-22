class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # special freq array where i is the freq value is list of nums w freq
        freq = [[] for i in range(len(nums) + 1)]
        # count map
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # populate the freq array
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # find top k from freq array
        for i in range(len(freq) - 1, 0, -1):
            # loop through num list for that freq
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
        

