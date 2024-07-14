from typing import List

from self import self


def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
    return len(list(filter(lambda h:h>=target, hours)))


hours = [0, 1, 2, 3, 4]
target = 2
print(numberOfEmployeesWhoMetTarget(self, hours, target))
