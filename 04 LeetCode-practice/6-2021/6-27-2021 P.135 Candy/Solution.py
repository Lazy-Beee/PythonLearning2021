"""
Day 5   6/27/2021-Sunday
Problem: https://leetcode.com/problems/candy/

There are n children standing in a line. Each child is assigned a rating value given in the
integer array ratings.
You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""


class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        ratings.append(int(1e5))
        candy = [1] * n

        def first_rating():
            if ratings[0] < ratings[1]:
                candy[0] = 1
                j = 0
                while True:
                    j += 1
                    if j > n-1:
                        break
                    if ratings[j-1] < ratings[j]:
                        candy[j] = candy[j-1] + 1
                    else:
                        break

        def update_right(j):
            candy[j] = 1
            while True:
                j += 1
                if j > n - 1:
                    break
                if ratings[j-1] < ratings[j] and candy[j] < candy[j-1] + 1:
                    candy[j] = candy[j-1] + 1
                else:
                    break

        def update_left(j):
            while True:
                j -= 1
                if j < 0:
                    break
                if ratings[j] > ratings[j+1] and candy[j] < candy[j+1] + 1:
                    candy[j] = candy[j+1] + 1
                else:
                    break

        for i in range(n):
            if i == 0:
                first_rating()
            else:
                if ratings[i - 1] >= ratings[i] and ratings[i] <= ratings[i + 1]:
                    update_right(i)
                    update_left(i)

        print(candy)
        return sum(candy)


if __name__ == "__main__":
    test = Solution()
    print(test.candy([1,2,4,4,3]))