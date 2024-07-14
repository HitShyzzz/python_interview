from typing import List

from self import self


def countTestedDevices(self, batteryPercentages: List[int]) -> int:
    need = 0
    for battery in batteryPercentages:
        # 当前元素需要减1的次数==前面已经测试过的电池数
        if battery > need:
            need += 1
    return need


batteryPercentages = [1, 1, 2, 1, 3]
print(countTestedDevices(self, batteryPercentages))
