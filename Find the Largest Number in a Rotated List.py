class Solution:
    def solve(self, arr):
        l, r = 0, len(arr) - 1
        m = (l+r)//2
        max_num = 0
        while l <= r:
            if arr[l] < arr[r]:
                max_num = max(arr[r], max_num)
            max_num = max(arr[m], max_num)
            print(l,m, r)
            # left sorted
            # 3 4 5 6 1 2
            # 0 1
            if arr[m] > arr[r]:
                l = m + 1
            # right sorted
            # 5 6 1 2 3 4
            else:
                r = m - 1
            
            m = (r + l)//2
        return max_num