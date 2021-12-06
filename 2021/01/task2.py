from collections import deque

from typing import Deque, Optional

result, prev = 0, 0
window: Deque[int] = deque()

f = open('input', 'r')
for line in f:
    value = int(line.strip())
    tmp_sum: Optional[int] = None

    window.append(value)

    if len(window) == 3:
        tmp_sum = sum(window)
        window.popleft()

        if tmp_sum and tmp_sum > prev and prev != 0:
            result += 1

    if tmp_sum:
        prev = tmp_sum

print(result)
