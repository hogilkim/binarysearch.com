class Solution:
    def solve(self, s0, s1):
        if len(s0) - len(s1) != 1:
            return False
        if s0[:-1] == s1:
            return True
        for i in range(len(s1)):
            if s0[i] != s1[i]:
                return s0[:i] + s0[i+1:] == s1


        return False



        # if len(s0) - len(s1) != 1:
        #     return False
        # diff = False
        # j = 0
        # for i in range (len(s0)):
        #     if diff==False and i == len(s0)-1:
        #         return True
        #     if diff and s0[i] != s1[j]:
        #         return False
        #     elif s0[i] != s1[j]:
        #         j -= 1
        #         diff = True
        #     j += 1
        # return diff
