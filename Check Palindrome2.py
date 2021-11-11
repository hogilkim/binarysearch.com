class Solution:
    def solve(self, s):
        return self.helper(0,len(s)-1, s)
    def helper(self,l,r,s):
        if s == "":
            return True
        if l >= r:
            return True
        return s[l] == s[r] and self.helper(l+1, r-1, s)