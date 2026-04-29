class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []
        closed = {')' : '(', '}' : '{', ']' : '[' }

        for character in s:
            if character in closed:
                if stack and stack[-1] == closed[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        
        return True if not stack else False