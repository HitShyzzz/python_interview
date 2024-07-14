from typing import Optional, List

from leetcode.高频面试题top150.递归回溯.TreeNode import TreeNode


def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def dfs(root: TreeNode):
        if root == None:
            return
        dfs(root.left)
        ans.append(root.val)
        dfs(root.right)

    dfs(root)
    return ans
