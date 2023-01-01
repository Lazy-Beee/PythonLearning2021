"""
Day 14   7/11/2021
Problem: https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two
characters may map to the same character, but a character may map to itself.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in dic.keys():
                    if t[i] in dic.values():
                        return False
                    dic[s[i]] = t[i]
                else:
                    if dic[s[i]] != t[i]:
                        return False
        return True


if __name__ == "__main__":
    test = Solution()
    str1 = 'badc'
    str2 = 'baba'
    print(test.isIsomorphic(str1, str2))