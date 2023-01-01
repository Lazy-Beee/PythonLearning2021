"""
Day 17   7/20/2021
Problem: https://leetcode.com/problems/reconstruct-original-digits-from-english/

Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
"""
import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        found = [0] * 10
        nums = {
            0: 'zero', 2: 'two', 4: 'four', 6: 'six', 8: 'eight',
            1: 'one', 3: 'three', 5: 'five', 7: 'seven', 9: 'nine'
        }
        letter = collections.defaultdict(int)
        for elem in s:
            letter[elem] += 1
        for num in nums:
            a = nums[num]
            c = True
            while c:
                for b in a:
                    if letter[b] < 1:
                        c = False
                if c:
                    for b in a:
                        letter[b] -= 1
                    found[num] += 1
        return ''.join([str(i) * found[i] for i in range(10)])


if __name__ == "__main__":
    test = Solution()
    print(test.originalDigits("owoztneoerone"))