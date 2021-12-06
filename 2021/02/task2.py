horizontal: int = 0
vertical: int = 0
aim: int = 0

with open("input", "r") as f:
    for line in f:
        instruction, value = line.split()

        match instruction:
            case "forward":
                horizontal += int(value)
                vertical += aim * int(value)
            case "up":
                aim -= int(value)
            case "down":
                aim += int(value)

print(horizontal * vertical)
