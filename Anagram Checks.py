class Solution:
    def solve(self, s0, s1):
        # Counter solution
        # from collection import Counter
        # O(n)
        # Space complexity: O(1)
        return Counter(s0) == Counter(s1)

        # sorting solution
        # O(log(n))
        # return sorted(s0) == sorted(s1)