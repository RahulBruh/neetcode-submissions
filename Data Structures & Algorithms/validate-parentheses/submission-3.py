class Solution:
    def isValid(self, s: str) -> bool:

        cuh = {")" : "(", "}" : "{", "]" :  "["}

        bruh = {"(","{","["}

        stack = []

        for i in range(len(s)):
            if s[i] in bruh:
                stack.append(s[i])
            
            else:
                if stack and cuh[s[i]] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False

        return True if not stack else False