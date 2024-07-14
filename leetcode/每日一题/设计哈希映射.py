
class MyHashMap:

    def __init__(self):
        self.datas = [[0] * 2] * 1001

    def put(self, key: int, value: int) -> None:
        x = hash(key)
        is_contain = False
        for data in self.datas:
            if x == data[0]:
                data[1] = value
                is_contain = True
                break
        if not is_contain:
            self.datas.append([key, value])

    def get(self, key: int) -> int:
        x = hash(key)
        for data in self.datas:
            if x == data[0]:
                return data[1]
        return -1

    def remove(self, key: int) -> None:
        x = hash(key)
        for data in self.datas:
            if x == data[0]:
                self.datas.remove(data)
                return

    def hash(key: int) -> int:
        return key % 1001
