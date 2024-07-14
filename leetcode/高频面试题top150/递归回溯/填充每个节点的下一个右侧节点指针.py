import collections


class Node:
    def __int__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# bfs 层序遍历
def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return root
    # 建立队列，并把根节点加入
    q = collections.deque([root])
    while q:
        size = len(q)
        for i in range(size):
            # 从队头取出元素
            node = q.popleft()
            # 只连接到size-2，那么每层最后一个元素的next指针指向的就是空！
            if i < size - 1:
                node.next = q[0]
            # 扩展下一层节点
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return root
