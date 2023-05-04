# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BST Property : 
# the left children of a node have a value smaller or equal to that of the node
# the right children of a node have a value bigger or equal to that of the node


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            v, pv, qv = root.val, p.val, q.val
            if v > max(pv, qv): root = root.left
            elif v < min(pv, qv): root = root.right
            else: return root