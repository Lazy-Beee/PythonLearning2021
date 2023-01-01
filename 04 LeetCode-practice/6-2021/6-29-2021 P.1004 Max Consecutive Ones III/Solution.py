"""
Day 7   6/29/2021
Problem: https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the
array if you can flip at most k 0's.
 """


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_count = 0
        a = 0
        b = 0

        for num in nums:
            b += 1
            if num == 0:
                k -= 1
                while k < 0:
                    if nums[a] == 0:
                        k += 1
                    a += 1

            max_count = max(max_count, b - a)
        return max_count

    def longestOnes_2(self, nums: list[int], k: int) -> int:
        start = 0
        for end in range(len(nums)):
            k -= (1 - nums[end])
            if k < 0:
                k += (1 - nums[start])
                start = start + 1
            print(f'k: {k}, start: {start}, end: {end}')
        return end - start + 1


if __name__ == "__main__":
    test = Solution()
    nums = [1,0,1,1,0,0,0,1,1,1,1,0,0,1,1]
    k = 2
    print(test.longestOnes(nums, k))
    print(test.longestOnes_2(nums, k))