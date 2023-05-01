def invertTree(self, root):
    if root:
        invert = self.invertTree
        root.left, root.right = invert(root.right), invert(root.left) # must invert concurrently to invert in the right order
        return root
    
