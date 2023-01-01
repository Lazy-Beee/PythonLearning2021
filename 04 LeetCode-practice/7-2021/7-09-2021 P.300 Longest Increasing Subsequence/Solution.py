"""
Day 13   7/09/2021
Problem: https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
"""
import bisect

import numpy as np


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        length = len(nums)
        dp = [[0 for _ in range(length+1)] for _ in range(length+1)]
        for i in range(1, length+1):
            for j in range(i, length+1):
                if nums[i-1] < nums[j-1]:
                    dp[j][i] = max(max(dp[i]) + 1, max(dp[j]))
        return max(max(row) for row in dp) + 1

    def lengthOfLIS2(self, nums: list[int]) -> int:
        sub = [nums[0]]
        for num in nums:
            if num > sub[-1]:
                sub.append(num)
            else:
                sub[bisect.bisect_left(sub, num)] = num
        return len(sub)



if __name__ == "__main__":
    test = Solution()
    nums = [0,1,0,3,2,3]
    print(test.lengthOfLIS(nums))