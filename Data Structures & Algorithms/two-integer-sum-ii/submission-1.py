class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted and ascending = binary O(n log n)
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            complement = target - numbers[i]
            while l <= r:
                mid = (r + l) // 2
                if numbers[mid] == complement:
                    return [i+1,mid+1]
                elif numbers[mid] < complement:
                    # current left options need to be updated
                    l = mid + 1
                elif numbers[mid] > complement:
                    # current right options need to be updated
                    r = mid - 1

