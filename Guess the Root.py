class Solution:
    def solve(self, n):
        l, r = 1, n
        middle = (l+r)//2

        while l <= r:
            result = ceil(middle*middle)
            print(result)
            if result == n:
                return middle
            if result < n:
                l = middle + 1
            else:
                r = middle - 1
            middle = (l+r)//2
        return middle
            