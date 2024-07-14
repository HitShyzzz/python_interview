from typing import Optional


class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_path = -30000001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)
            cur_max = root.val + left_max + right_max
            self.max_path = max(self.max_path, cur_max)
            return root.val + max(left_max, right_max)

        dfs(root)
        return self.max_path
