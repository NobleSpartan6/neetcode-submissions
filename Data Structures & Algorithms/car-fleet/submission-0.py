class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a pair array
        pair = [[p,s] for p, s in zip(position,speed)]
        
        stack = []
        for p, s in sorted(pair)[::-1]:  # Reverse Sorted Order
            stack.append((target - p) / s)
            # ensure stack has 2 elements and check if the car behind collides with car ahead
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)