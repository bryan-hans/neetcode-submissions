class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []

        for p in s:
            if p not in matches:
                stack.append(p)
            else:
                if not stack or stack[-1] != matches[p]:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0
