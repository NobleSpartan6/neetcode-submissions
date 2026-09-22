class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) - 1

        while a <= b:
            mid = (a+b) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= target:
                b = mid - 1
            else:
                a = mid + 1
        return -1 