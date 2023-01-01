import bisect

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2

            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid
            print(lo, hi)
        return lo


test = Solution()
print(test.kthSmallest([[1,1,9],[10,11,13],[12,13,15]], 4))