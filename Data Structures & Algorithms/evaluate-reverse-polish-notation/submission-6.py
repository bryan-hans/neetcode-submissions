class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for letter in tokens:
            if letter not in operators:
                stack.append(int(letter))
            else:
                b = stack.pop()
                a = stack.pop()
                if letter == '+':
                    stack.append(a + b)
                elif letter == '-':
                    stack.append(a - b)
                elif letter == '*':
                    stack.append(a * b)
                elif letter == '/':
                    stack.append(int(a / b))
        return stack[-1]