class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens: 
            if s not in {"+", "-", "*", "/"}:
                stack.append(int(s))
            elif stack:
                second = stack.pop()
                first = stack.pop()
                if s == "+":
                    stack.append(first + second)
                elif s == "*":
                    stack.append(first * second)
                elif s == "/":
                    stack.append(int(first / second))
                elif s == "-":
                    stack.append(first - second)

        return stack[0]
                
                