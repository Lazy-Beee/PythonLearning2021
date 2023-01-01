"""
Day 4   6/25/2021-Friday
Problem: https://leetcode.com/problems/split-a-string-in-balanced-strings/

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.
"""
import time


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        start_time = time.time()
        b, c = 0, 0
        for a in s:
            if a == "R":
                b += 1
            else:
                b -= 1

            if b == 0:
                c += 1
        print(f"Time: {1000 * (time.time() - start_time)} ms")
        return c


if __name__ == '__main__':
    test = Solution()
    print(test.balancedStringSplit("RLRRRLLRLLRLRRRLLRLLRLRRRLLRLLRLRRRLLRLLRLRRRLLRLLRLRRRLLRLL"))
