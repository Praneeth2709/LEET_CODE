class Solution:
    def inorderTraversal(self, root):
        result = []

        def walk(node):
            if not node:
                return

            walk(node.left)       # LEFT
            result.append(node.val) # ME
            walk(node.right)      # RIGHT

        walk(root)
        return result