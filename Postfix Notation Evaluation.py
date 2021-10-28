class Solution:
    def solve(self, exp):
        stack = []
        if len(exp) > 0:
            stack.append(int(exp[0]))
        if len(exp) > 1:
            stack.append(int(exp[1]))
        i = 2

        while i <len(exp):
            if exp[i] in "*+-/":
                val2 = stack.pop()
                val1 = stack.pop()
                if exp[i] == "+":
                    stack.append(val1 + val2)
                elif exp[i] == "-":
                    stack.append(val1 - val2)
                elif exp[i] == "*":
                    stack.append(val1 * val2)
                else:
                    res = val1/val2
                    if res >0:
                        res = floor(res)
                    else:
                        res = ceil(res)
                    stack.append(res)
            else:
                stack.append(int(exp[i]))
            i += 1
        return stack[-1]

        # while i < len(exp):
        #     if exp[i] == "+":
        #         res = stack[-1] + stack[-2]
        #         stack.pop()
        #         stack.pop()
        #         stack.append(res)
        #     elif exp[i] == "-":
        #         res = stack[-2] - stack[-1]
        #         stack.pop()
        #         stack.pop()
        #         stack.append(res)
        #     elif exp[i] == "*":
        #         res = stack[-2] * stack[-1]
        #         stack.pop()
        #         stack.pop()
        #         stack.append(res)
        #     elif exp[i] == "/":
        #         res = stack[-2] / stack[-1]
        #         if res > 0:
        #             res = floor(res)
        #         else:
        #             res = ceil(res)
        #         stack.pop()
        #         stack.pop()
        #         stack.append(res)
        #     else:
        #         stack.append(int(exp[i]))
        #    i += 1
        #return stack[-1]