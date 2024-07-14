from typing import Optional


class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # maxPath表示的是以cur节点为根节点，同时以cur为起点的子节点最大路径之和
        def maxPath(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left_max = max(maxPath(self, root.left), 0)
            right_max = max(maxPath(self, root.right), 0)

            # 当前节点的最大路径之和
            cur_max_sum = root.val + left_max + right_max
            self.max_sum = max(self.max_sum, cur_max_sum)

            return root.val + max(left_max, right_max)

        maxPath(self, root)
        return self.max_sum
