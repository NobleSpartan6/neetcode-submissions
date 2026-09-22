class Solution:
    def isValid(self, s: str) -> bool:
        # last in first out (stack order)
        stack = []
        closeToOpen = {")" : "(", "]" :"[", "}":"{"}
        
        for c in s:
            # check if c is a closing pair // edge case
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack
