"""
Day 12   7/08/2021
Problem: https://leetcode.com/problems/array-of-doubled-pairs/

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
"""
import numpy as np


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        len1, len2 = len(nums1) + 1, len(nums2) + 1
        dp = [[0 for _ in range(len2)] for _ in range(len1)]
        for i in range(1, len1):
            for j in range(1, len2):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(row) for row in dp)


if __name__ == "__main__":
    test = Solution()
    nums1 = [1,0,0,0,1]
    nums2 = [1,0,0,1,1]
    print(test.findLength(nums1, nums2))