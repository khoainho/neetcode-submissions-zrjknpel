# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.good_nodes = 0 
        self.dfs(root, -10001)

        return self.good_nodes

    def dfs(self, node, max_seen):
        if not node:
            return None
        
        if node.val >= max_seen:
            self.good_nodes += 1
            max_seen = max(node.val, max_seen)

        self.dfs(node.left, max_seen)
        self.dfs(node.right, max_seen)