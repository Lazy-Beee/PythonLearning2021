"""
Day 6   6/28/2021
Problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

You are given a string s consisting of lowercase English letters. A duplicate removal consists of
choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that
the answer is unique.
 """
from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for letter in s:
            if ans:
                if letter == ans[-1]:
                    ans.pop()
                    continue
            ans.append(letter)
        return ''.join(ans)

    def removeDuplicates_2(self, s: str) -> str:
        dup = [2 * ch for ch in ascii_lowercase]
        l = -1
        while l != len(s):
            l = len(s)
            for d in dup:
                s = s.replace(d, '')
        return s


if __name__ == "__main__":
    test = Solution()
    print(test.removeDuplicates("abbaca"))