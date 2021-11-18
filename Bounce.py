class Solution:
    def solve(self, nums, k):
        visited = set()
        def dfs(index):
            if index in visited:
                return False
            if index == len(nums)-1:
                return True
            elif index > len(nums) - 1:
                return False
            elif index < 0:
                return False
            steps = nums[index]
            if steps == 0:
                return False
            visited.add(index)
            return dfs(index + steps) or dfs(index - steps)

        return dfs(k)