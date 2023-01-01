"""
Day 11   7/07/2021
Problem: https://leetcode.com/problems/array-of-doubled-pairs/

Given an array of integers arr of even length, return true if and only if it is possible to reorder it such that
arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.
"""
import collections


class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        arr.sort()
        while arr:
            num = arr[0]
            if num > 0:
                if num*2 in arr:
                    arr.remove(num)
                    arr.remove(num*2)
                else:
                    return False
            elif num < 0:
                if num/2 in arr:
                    arr.remove(num)
                    arr.remove(num/2)
                else:
                    return False
            else:
                if arr.count(0) % 2 == 0:
                    arr.remove(0)
                    arr.remove(0)
                else:
                    return False
        return True

    def canReorderDoubled2(self, arr: list[int]) -> bool:
        arr.sort()
        integer = collections.defaultdict(int)
        count = 0
        for elem in arr:
            if integer[elem*2] > 0:
                integer[elem*2] -= 1
            elif integer[elem/2] > 0:
                integer[elem/2] -= 1
            else:
                integer[elem] += 1
                count += 1

        return count == len(arr)/2


if __name__ == "__main__":
    test = Solution()
    arr = [1,2,4,8]
    print(test.canReorderDoubled2(arr))