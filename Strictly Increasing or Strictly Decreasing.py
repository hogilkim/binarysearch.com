class Solution:
    def solve(self, nums):
        is_sorted = sorted(nums)==nums
        is_reverse_sorted = sorted(nums, reverse=True) == nums
        is_unique = len(set(nums)) == len(nums)

        return is_unique and (is_sorted or is_reverse_sorted)
        
        
        # if len(nums) <= 1:
        #     return True
        # increasingDecreasing = 3
        # if nums[0] > nums[1]:
        #     increasingDecreasing = 2
        # elif nums[0] < nums[1]:
        #     increasingDecreasing = 1
        # else: 
        #     return False
        # new_increasingDecreasing = 0
        # for i in range(1, len(nums)-1):
        #     if nums[i] < nums[i+1]:
        #         new_increasingDecreasing = 1
        #     elif nums[i] > nums[i+1]:
        #         new_increasingDecreasing = 2
        #     else:
        #         return False
        #     if new_increasingDecreasing != increasingDecreasing:
        #         return False
            
        # return True