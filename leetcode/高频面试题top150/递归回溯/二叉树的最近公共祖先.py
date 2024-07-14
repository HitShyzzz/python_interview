class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    ans = None

    # 返回以root为根结点的子树是否包含p或者q结点
    def dfs(root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if not root:
            return False
        l_sin = dfs(root.left, p, q)
        r_sin = dfs(root.right, p, q)
        if (l_sin and r_sin) or (root.val == p.val or root.val == q.val and (l_sin or r_sin)):
            self.ans = root
        return l_sin or r_sin or root.val == p.val or root.val == q.val

    dfs(root, p, q)
    return self.ans
