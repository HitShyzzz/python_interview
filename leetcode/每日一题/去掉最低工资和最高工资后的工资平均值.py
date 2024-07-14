from typing import List

from self import self


def average(self, salary: List[int]) -> float:
    return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)


salary = [8000, 9000, 2000, 3000, 6000, 1000]
print(average(self, salary))
