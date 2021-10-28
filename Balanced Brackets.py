class Solution:
    def solve(self, s):
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack:
                    return False
                stack.pop()
        if not stack:
            return True
        return False