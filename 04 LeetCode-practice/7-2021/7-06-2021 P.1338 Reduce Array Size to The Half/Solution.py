"""
Day 10   7/06/2021
Problem: https://leetcode.com/problems/reduce-array-size-to-the-half/

Given an array arr.  You can choose a set of integers and remove all the occurrences of these
integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
"""


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        integers = {}
        for elem in arr:
            if elem not in integers.keys():
                integers[elem] = 1
            else:
                integers[elem] += 1
        integers_sorted = {k: v for k, v in sorted(integers.items(), key=lambda item: item[1],
                                                   reverse=True)}
        count = 0
        remove = 0
        for v in integers_sorted.values():
            count += 1
            remove += v
            if remove >= len(arr)/2:
                return count

    def minSetSize2(self, arr: list[int]) -> int:
        integers = {}
        for elem in arr:
            if elem not in integers.keys():
                integers[elem] = 1
            else:
                integers[elem] += 1
        int_num = list(integers.values())
        int_num.sort(reverse=True)
        count = 0
        remove = 0
        while remove < len(arr)/2:
            remove += int_num[count]
            count += 1
        return count


if __name__ == "__main__":
    test = Solution()
    arr = [3,3,3,3,5,5,5,2,2,7]
    print(test.minSetSize2(arr))