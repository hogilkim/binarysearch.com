class Solution:
    def solve(self, nums):
        return 0 if not nums else max(Counter(nums).values())
        # if len(nums) < 1:
        #     return 0
        # sorted_list = sorted(nums)
        # max_count = 1
        # curr_count = 1
        # for i in range(1, len(sorted_list)):
        #     if sorted_list[i-1] == sorted_list[i]:
        #         curr_count += 1
        #         max_count = max(max_count, curr_count)
        #     else:
        #         curr_count = 1
        # return max_count
