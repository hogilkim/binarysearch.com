class Solution:
    def solve(self, s):
        

        # set solution
        previous_ch = set()
        for i in range(s):
            # searching in set is constant time
            if s[i] in previous_ch:
                return i
            previous_ch.add(s[i])
        return -1

        # dict solution
        # mp = {}
        # if len(s) == 0:
        #     return -1
        # i = 0
        # for ch in s:
        #     if ch not in mp:
        #         mp[ch] = 1
        #         i += 1
        #     elif ch in mp:
        #         return i
        # if i == len(s):
        #     return -1