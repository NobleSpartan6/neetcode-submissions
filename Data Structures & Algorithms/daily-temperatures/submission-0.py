class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rizz = [0] * len(temperatures)

        stack = [] # pair [t, i]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                rizz[stackIdx] = (i - stackIdx)
            stack.append([t,i])
        
        return rizz




