class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                v1 = stack.pop()
                v2 = stack.pop()
                v3 = v2 + v1
                stack.append(v3)
            elif t == '-':
                v1 = stack.pop()
                v2 = stack.pop()
                v3 = v2 - v1
                stack.append(v3)
            elif t == '*':
                v1 = stack.pop()
                v2 = int(stack.pop())
                v3 = v2 * v1
                stack.append(v3)
            elif t == '/':
                v1 = stack.pop()
                v2 = stack.pop()
                v3 = int(v2 / v1)
                stack.append(v3)
            else:
                stack.append(int(t))
        return stack[0]