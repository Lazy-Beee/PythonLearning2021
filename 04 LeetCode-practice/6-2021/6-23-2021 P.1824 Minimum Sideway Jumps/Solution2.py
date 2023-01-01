"""
Day 2   6/22/2021-Wednesday
Problem: https://leetcode.com/problems/minimum-sideway-jumps/
"""


class Solution:
    def minSideJumps(self, obstacles: list[int]) -> int:
        steps = [1, 0, 1]
        obstacles.append(0)
        for i in range(1, len(obstacles)-1):
            new_steps = [0, 0, 0]
            if obstacles[i]:
                new_steps[obstacles[i] - 1] = float('inf')
            if obstacles[i+1]:
                new_steps[obstacles[i+1] - 1] = float('inf')

            for route in range(3):
                steps_temp = []
                if route != obstacles[i] - 1 and route != obstacles[i+1] - 1:
                    for j in range(3):
                        if j == route:
                            steps_temp.append(steps[j]-1)
                        else:
                            steps_temp.append(steps[j])
                    new_steps[route] = min(steps_temp) + 1
            steps = new_steps

        return min(steps)


test = Solution()
print(test.minSideJumps([0,2,1,0,3,0]))

"""
    steps = [1, 0, 1]
        for i in range(1, len(obstacles)-1):
            if obstacles[i]:
                steps[obstacles[i] - 1] = float('inf')

            for route in range(3):
                if route != obstacles[i] - 1:
                    steps[route] = min(steps[route]-1, steps[(route +1)%3], steps[(route +2)%3]) + 1

        return min(steps)
"""
