class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        out = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                    out = max(out, len(stack))
                    if stack:stack.pop()
                        
        return out
