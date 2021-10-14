class Solution:
    def solve(self, nums, k):
            
        new_list = []
        new_list=nums[k:]+ nums[:k]
        return new_list