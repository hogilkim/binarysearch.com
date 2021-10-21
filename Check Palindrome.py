class Solution:
    def solve(self, s):
        length = len(s)
        if length < 2:
            return True

        middle = 0
        if length % 2 == 1:
            middle = int(length/2)
            second_substring = s[middle+1:]
            return s[:middle] == second_substring[::-1]
        else:
            middle = int(length/2-1)
            second_substring = s[middle+1:]
            return s[:middle+1] == second_substring[::-1]
