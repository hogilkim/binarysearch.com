class Solution:
    def solve(self, nums):
        return any(key==val for key, val in Counter(nums).items())
        # num_dict = {}
        # for num in nums:
        #     if num in num_dict:
        #         num_dict[num] += 1
        #     else:
        #         num_dict[num] = 1
        
        # for num in num_dict:
        #     if num_dict[num] == num:
        #         return True
        # return False