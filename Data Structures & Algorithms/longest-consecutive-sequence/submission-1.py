class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn num list into set
        numSet = set(nums)
        max_length = 0
        # check for the start of sequence 
        for n in nums: 
            # check if this is the start of a sequence
            if n-1 not in numSet:
                curr = n
                curr_len = 1
                while curr+1 in numSet: 
                    curr += 1
                    curr_len += 1
                max_length = max(max_length, curr_len)
        
        return max_length
