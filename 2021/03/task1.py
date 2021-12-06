from typing import List

# represent count of 0 and 1's as
result: List[List[int]] = [[0] * 2 for _ in range(12)]

with open("input", "r") as f:
    for line in f:
        line = line.strip()

        for i in range(len(line)):
            result[i][int(line[i])] += 1

gamma: List[int] = list()
epsilon: List[int] = list()

for i in range(len(result)):
    if result[i][0] > result[i][1]:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

# TODO: convert back to int in a nicer way
print(int("".join([str(i) for i in gamma]), 2) * int("".join([str(i) for i in epsilon]), 2))
