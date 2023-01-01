"""
Day 16   7/19/2021
Problem: https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to
n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector
rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction
(See the first example).
"""
import collections


class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        count = collections.defaultdict(int)
        count[rounds[-1] % n] += 1
        for i in range(len(rounds)-1):
            a, b = rounds[i], rounds[i+1]
            if b <= a:
                b += n
            for x in range(a, b):
                count[x % n] += 1
        max_count = max(count.values())
        ans = []
        print(count)
        for k in count:
            if count[k] == max_count:
                if k == 0:
                    k += n
                ans.append(k)
        ans.sort()
        return ans


if __name__ == "__main__":
    test = Solution()
    print(test.mostVisited(2, [2,1,2,1,2,1,2,1,2]))