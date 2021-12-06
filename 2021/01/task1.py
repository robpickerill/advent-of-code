from typing import Optional

f = open('input', 'r')

result = 0
prev: Optional[int] = None

for line in f:
    try:
        value = int(line.strip())
    except ValueError:
        continue

    if prev and value > prev:
        result += 1

    prev = value

print(result)
