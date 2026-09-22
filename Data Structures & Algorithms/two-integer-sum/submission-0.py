class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = {}
        # hashmap where 
        # [number : index]

        for i in range(len(nums)):
            complement = target - nums[i]
            # check if complement is already in 
            if complement in twosum:
                return [twosum[complement], i]
            else: 
                twosum[nums[i]] = i
        