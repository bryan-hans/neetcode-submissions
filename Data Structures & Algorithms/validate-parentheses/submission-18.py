class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []

        for p in s:
            if p in matches:
                if stack and stack[-1] == matches[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        if stack:
            return False
        else:
            return True