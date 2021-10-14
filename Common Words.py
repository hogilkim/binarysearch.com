class Solution:
    def solve(self, s0, s1):
        return len( set(s0.lower().split()) & set(s1.lower().split() ) )     
        
        # s0_list = s0.lower().split()
        # s1_list = s1.lower().split()
        # s0_set = set(s0_list)
        # s1_set = set(s1_list)

        # count = 0
        # for word in s0_set:
        #     if word in s1_set:
        #         count += 1
        # return count

