class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count each element {key: num value is freq}
        count = {}
        # special array where i is the freq and values is list of nums w that freq   
        freq = [[] for i in range(len(nums) + 1)]
        
        # count the freq of nums
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
        # populate the special freq array
        for n,c in count.items(): 
            freq[c].append(n)
        
        # find the top k elements
        res = []
        # loop in descending order 
        for i in range(len(freq) - 1, 0, -1):
            # loop through the list of values for that freq at i 
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res