class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}

        for i in tokens:
            if i in operations:
                val2 = stack.pop()
                val1 = stack.pop()
                if i == "+":
                    stack.append(val1 + val2)
                elif i == "-":
                    stack.append(val1 - val2)
                elif i == "*":
                    stack.append(val1 * val2)
                elif i == "/":
                    stack.append(int(val1/val2))
                
            else:
                stack.append(int(i))

        return stack[0]