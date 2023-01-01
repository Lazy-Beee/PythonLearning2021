"""
Day 8   6/30/2021
Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a
node to be a descendant of itself).”
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        tree = root.val
        p_val = p.val
        q_val = q.val

        def find_par(ind):
            n = 0
            while True:
                if ind - 2 ** n < 0:
                    break
                else:
                    ind -= 2 ** n
                    n += 1
            par = []
            while n >= 0:
                par.insert(0, tree[2**n - 1 + ind])
                print(n, ind)
                n -= 1
                ind = ind // 2
            return par

        p_par = find_par(tree.index(p_val))
        q_par = find_par(tree.index(q_val))

        for i in range(min(len(p_par), len(q_par))):
            if p_par[i] != q_par[i]:
                break

        return TreeNode(p_par[i-1])


if __name__ == "__main__":
    test = Solution()
    root = TreeNode([3,5,1,6,2,0,8,None,None,7,4])
    p = TreeNode(6)
    q = TreeNode(7)
    print(test.lowestCommonAncestor(root, p, q).val)