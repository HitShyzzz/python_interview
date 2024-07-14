from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(root: TreeNode, upper=float('inf'), lower=float('-inf')) -> bool:
        if not root:
            return True
        cur = root.val
        if cur <= lower or cur >= upper:
            return False
        left_valid = dfs(root.left, cur, lower)
        right_valid = dfs(root.right, upper, cur)
        return left_valid and right_valid

    return dfs(root)
