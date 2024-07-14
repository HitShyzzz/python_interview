# 自定义哈希函数，使用链地址法解决哈希冲突
class MyHashSet:

    def __init__(self):
        self.BASE = 1001
        self.data = [[]] * self.BASE

    def add(self, key: int) -> None:
        x = self.hash(key)
        if key in self.data[x]:
            return
        self.data[x].append(key)

    def remove(self, key: int) -> None:
        x = self.hash(key)
        if key not in self.data[x]:
            return
        self.data[x].remove(key)

    def contains(self, key: int) -> bool:
        x = self.hash(key)
        if key in self.data[x]:
            return True
        return False

    def hash(self, key: int):
        return key % self.BASE
