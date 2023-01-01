"""
Day 18   7/24/2021
Problem: https://leetcode.com/problems/4sum-ii/

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l)
such that: 0 <= i, j, k, l < n; nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""
import collections


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        cnt1, cnt2, ans = collections.defaultdict(int), collections.defaultdict(int), 0
        for a in nums1:
            for b in nums2:
                cnt1[a + b] += 1
        for c in nums3:
            for d in nums4:
                cnt2[c + d] += 1
        for val in cnt1:
            if -val in cnt2:
                ans += cnt1[val] * cnt2[-val]
        return ans


if __name__ == "__main__":
    test = Solution()
    print(test.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))