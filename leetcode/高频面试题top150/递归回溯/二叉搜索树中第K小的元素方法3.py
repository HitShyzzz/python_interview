from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # 记录以root作为根节点的总共节点数
    def dfs(root: TreeNode) -> int:
        if not root:
            return 0
        left_cnt = dfs(root.left)
        right_cnt = dfs(root.right)
        return left_cnt + right_cnt + 1

    left_cnt = dfs(root.left)
    # 第k小元素在右子树
    if left_cnt < k - 1:
        return self.kthSmallest(root.right, k - left_cnt - 1)
    # 第k小元素等于root节点
    elif left_cnt == k - 1:
        return root.val
    # 第k小元素在左子树
    else:
        return self.kthSmallest(root.left, k)
