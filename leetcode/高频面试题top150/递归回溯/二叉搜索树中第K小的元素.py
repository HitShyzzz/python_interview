import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    list = []

    def dfs(root: TreeNode, visited: int):
        if not root:
            return

        dfs(root.left, visited)
        list.append(root.val)
        dfs(root.right, visited)

    dfs(root, 0)
    return list[k - 1]
