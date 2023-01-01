"""
Day 14   7/14/2021
Problem: https://leetcode.com/problems/custom-sort-string/

order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order
that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned
string.

Return any permutation of str (as a string) that satisfies this property.
"""
import collections


class Solution:
    def customSortString(self, o: str, s: str) -> str:
        count = collections.defaultdict(int)
        output = ""
        seen = set()
        for letter in s:
            if letter in count.keys():
                count[letter] += 1
            else:
                count[letter] = 1
        for letter in o:
            if letter in count.keys():
                output += str(letter) * count[letter]
                seen.add(letter)
        for letter in count.keys():
            if letter not in seen:
                output += str(letter) * count[letter]

        return output


if __name__ == "__main__":
    test = Solution()
    print(test.customSortString("cba", "abcdabdcfr"))