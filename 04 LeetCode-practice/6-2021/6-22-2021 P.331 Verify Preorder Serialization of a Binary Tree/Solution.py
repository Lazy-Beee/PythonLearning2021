"""
Day 1   6/22/2021-Tuesday
Problem: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        preorder = preorder.split(",")

        for item in preorder:
            # Avoid input preorder of [#]
            if stack == ['#']:
                return False

            # Check whether a node is clear, is yes, replace the three items with "#"
            stack.append(item)
            while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#":
                if stack[-3] != "#":
                    stack = stack[:-3]
                    stack.append("#")
                # Return false if three "#" in row
                else:
                    return False

        # If stack is [#], return true
        if stack == ["#"]:
            return True
        else:
            return False


test = Solution()
print(test.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))




