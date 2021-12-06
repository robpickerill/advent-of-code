forward: int = 0
vertical: int = 0

with open("input", "r") as f:
    for line in f:
        instruction, value = line.split()

        match instruction:
            case "forward":
                forward += int(value)
            case "up":
                vertical -= int(value)
            case "down":
                vertical += int(value)

print(forward * vertical)
