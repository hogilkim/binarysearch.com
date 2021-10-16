class Solution:
    def solve(self, nums):
        return sum(len(str(num))% 2 for num in nums)