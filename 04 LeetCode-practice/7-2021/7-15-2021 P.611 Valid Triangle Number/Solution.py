"""
Day 15   7/15/2021
Problem: https://leetcode.com/problems/valid-triangle-number/

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take
them as side lengths of a triangle.
"""
import collections


class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        count = 0
        nums.sort()
        for i, num1 in enumerate(nums[:-2]):
            for j, num2 in enumerate(nums[i+1:-1]):
                count += sum(1 for x in nums[i+j+2:] if x < num1 + num2)
        return count

    def triangleNumber2(self, nums: list[int]) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] != 0:
                k = i + 2
                for j in range(i + 1, len(nums) - 1):
                    while k < len(nums) and nums[i] + nums[j] > nums[k]:
                        k += 1
                    count += k - j - 1
        return count


if __name__ == "__main__":
    test = Solution()
    print(test.triangleNumber2([2,2,3,4]))