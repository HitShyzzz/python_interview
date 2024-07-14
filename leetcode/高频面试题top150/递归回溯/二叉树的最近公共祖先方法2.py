import collections


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parent = {}
    visited = []

    # 1、记录每个结点的父结点
    def dfs(root: TreeNode):
        if not root:
            return
        if root.left:
            parent[root.left] = root
            dfs(root.left)
        if root.right:
            parent[root.right] = root
            dfs(root.right)

    dfs(root)
    # 2、自底向上去记录p的父结点
    while p:
        visited.append(p)
        p = parent.get(p)
    # 3、自底向上遍历q的父节点，当q的父结点首次首先在q的父结点列表中时，就一定是最近公共祖先
    while q:
        if q in visited:
            return q
        q = parent.get(q)
