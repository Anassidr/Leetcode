# Top down approach : O(n^2) complexity 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if abs(right_height - left_height) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left) 

    def height(self, root):
        if root is None:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        return max(left_height, right_height) + 1

# eliminating repeated work to have O(n)
# bottom up approach 
# For each node we keep track of two things : are the subtrees of the node balanced, what is the height of the node

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(right[1]-left[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]