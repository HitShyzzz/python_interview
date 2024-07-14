from typing import List

from self import self


def countTestedDevices(self, batteryPercentages: List[int]) -> int:
    n = len(batteryPercentages)
    cnt = 0
    for i in range(n):
        if batteryPercentages[i] > 0:
            cnt += 1
            for j in range(i + 1, n):
                batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
    return cnt


batteryPercentages = [1, 1, 2, 1, 3]
print(countTestedDevices(self, batteryPercentages))
