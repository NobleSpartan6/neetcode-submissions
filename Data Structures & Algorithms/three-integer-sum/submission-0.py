class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i + j + k = 0
        # i,j,k -> set 

        # sort the array to find complement

        # [-1, 0, 1, 2, -1, -4]
        # [-4, -1, -1, 0, 1 ,2]
        # i = 0
        # -4 -> complement 4

        threeSum = set()
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            j, k = i+1, len(nums) - 1
            while j < k:
                if nums[i] + nums[k] + nums[j] < 0:
                    j += 1
                elif nums[i] + nums[k] + nums[j] > 0:
                    k -= 1
                elif nums[i] + nums[k] + nums[j] == 0:
                    # tuple 
                    triplet = (nums[i], nums[j], nums[k])
                    # check if tuple is not in threeSum so we can append it to our result
                    if triplet not in threeSum:
                        res.append([nums[i], nums[j], nums[k]])
                        threeSum.add(triplet)
                    j += 1
                    k -= 1
        return res
