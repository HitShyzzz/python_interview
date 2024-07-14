from typing import Optional


class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def dfs(left: TreeNode, right: TreeNode) -> bool:
        # 左右节点都为空
        if not (left or right):
            return True
        # 左右节点有一个为空
        if not (left and right):
            return False
        # 左右节点值不相等
        if left.val != right.val:
            return False
        return dfs(left.left, right.right) and dfs(left.right, right.left)

    return dfs(root.left, root.right)
