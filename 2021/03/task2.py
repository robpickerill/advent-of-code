from typing import List, Tuple
from enum import Enum

class Gas(Enum):
    O2 = 1
    CO2 = 2


def input() -> List[str]:
    with open("input", "r") as f:
        return f.read().splitlines()


def counter(readings: List[str], column: int) -> Tuple[int, int]:
    num_0, num_1 = 0, 0

    for i in range(len(readings)):
        match int(readings[i][column]):
            case 0: num_0 += 1
            case 1: num_1 += 1

    return (num_0, num_1)


def reduce(readings: List[str], gas_type: Gas) -> str:
    for i in range(len(readings[0])):

        if len(readings) == 1:
            return readings[0]

        num_0, num_1 = counter(readings, i)

        match gas_type:
            case Gas.O2:
                if num_1 >= num_0:
                    readings = list(filter(lambda x: int(x[i]) == 1, readings))
                else:
                    readings = list(filter(lambda x: int(x[i]) == 0, readings))

            case Gas.CO2:
                if num_1 >= num_0:
                    readings = list(filter(lambda x: int(x[i]) == 0, readings))
                else:
                    readings = list(filter(lambda x: int(x[i]) == 1, readings))

    if len(readings) == 1:
        return readings[0]
    else:
        raise ValueError("???")


data = input()
o2 = reduce(data.copy(), Gas.O2)
co2 = reduce(data.copy(), Gas.CO2)

print(int(o2, 2) * int(co2, 2))
