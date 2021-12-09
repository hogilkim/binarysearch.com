class Solution:
    def solve(self, message):
        if message[0] == "0":
            return 0
        dp = [1 for i in range(len(message)+1)]

        for i in range(2, len(dp)):
            if message[i-1] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            
            if 10<= int(message[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
        