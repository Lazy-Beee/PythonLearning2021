"""
Day 4   6/25/2021-Friday
Problem: https://leetcode.com/problems/wiggle-sort-ii/

Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.
"""
class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i = 0
        a = 1 - len(nums) % 2
        while len(nums) - i >= 2:
            j = (len(nums)+i)//2 - a
            nums.insert(i, nums[j])
            nums.insert(i + 1, nums[-1])
            nums.pop(j + 2)
            nums.pop(-1)
            i += 2
        return nums

    def wiggleSort2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums_sort = sorted(nums, reverse=True)
        for i in range(n):
            if i % 2:
                nums[i] = nums_sort[i//2]
            else:
                nums[i] = nums_sort[n//2+i//2]

        return nums


if __name__ == '__main__':
    test = Solution()
    print(test.wiggleSort2([1,5,1,1,6,4]))
