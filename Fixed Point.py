class Solution:
    def solve(self, nums):
        l, r = 0, len(nums)-1
        ans = -1
        while l <= r:
            m = (l+r)//2
            if nums[m] == m:
                ans = m
            if nums[m] < m:
                l = m + 1
            else:
                r = m - 1
            m = (l+r)//2
        return ans