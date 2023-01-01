"""
Day 8   7/02/2021
Problem: https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the
array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 """
import bisect


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        if len(arr) == 1:
            return arr
        elif k == 1:
            abs_arr = [abs(a-x) for a in arr]
            pos = abs_arr.index(min(abs_arr))
            return [arr[pos]]

        start = 0
        for i in range(len(arr) - k):
            if abs(arr[i] - x) <= abs(arr[i+k] - x) and arr[i+k] - x >= 0:
                start = i
                break
            start = i+1
        return arr[start:start+k]


if __name__ == "__main__":
    test = Solution()
    arr = [1,1,1,10,10,10]
    k = 1
    x = 10
    print(test.findClosestElements(arr, k, x))