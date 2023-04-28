#inorder traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> int:
        values = []
        if root:
            values += self.inorderTraversal(root.left)
            values.append(root.val)
            values += self.inorderTraversal(root.right)
        return values
