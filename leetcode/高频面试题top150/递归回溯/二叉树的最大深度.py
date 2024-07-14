from typing import Optional


class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


def maxDepth(self, root: Optional[TreeNode]) -> int:
    import functools
    @functools.lru_cache(None)
    def dfs(root: TreeNode) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root)
