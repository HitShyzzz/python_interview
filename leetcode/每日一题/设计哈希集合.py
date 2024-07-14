import functools


class MyHashSet:

    def __init__(self):
        self.list = []

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.list.append(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        self.list.remove(key)

    @functools.lru_cache(None)
    def contains(self, key: int) -> bool:
        if key in self.list:
            return True
        return False
