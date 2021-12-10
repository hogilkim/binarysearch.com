class Solution:
    def solve(self, prices, n):
        dp = [0]

        for rod_size in range(1, n+1):
            max_profit = 0
            for final_piece in range(1, rod_size+1):
                max_profit = max(max_profit, 
                    dp[rod_size - final_piece]+prices[final_piece-1])
            dp.append(max_profit)
        return dp[-1]