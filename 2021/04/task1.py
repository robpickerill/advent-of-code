from typing import Optional


# type aliases
Board = list[list[int]]
Grid = list[Board]
Cache = dict[int, list[tuple[int, int, int]]]


def read_input() -> list[str]:
    with open("2021/04/input", "r") as f:
        return f.read().splitlines()


def parse_nums(input: str) -> list[int]:
    return [int(x) for x in input.split(",")]


def parse_grid(input: list[str]) -> tuple[Grid, Cache]:
    grid: Grid = []
    board: Board = []
    cache: Cache = {}

    n = 0
    while n < len(input):
        row: list[int] = []

        if input[n]:
            for i, v in enumerate(input[n].split()):
                v_ = int(v)
                row.append(v_)

                # cache numbers, with locations in the grid
                location = (len(grid), n % 6, i)
                if cache.get(v_):
                    cache[v_].append(location)
                else:
                    cache[v_] = [location]

            board.append(row)

        else:
            grid.append(board.copy())
            board.clear()

        n += 1

    # if there is no trailing empty line
    if board:
        grid.append(board.copy())

    return (grid, cache)


def is_winner(grid: Grid, board_i: int, row_i: int, i: int) -> bool:
    if (
        sum(grid[board_i][row_i]) == -5
        or sum([grid[board_i][vert_i][i] for vert_i in range(5)]) == -5
    ):
        return True

    return False


def mark_numbers(grid: Grid, cache: Cache, number: int) -> tuple[Grid, Optional[int]]:
    locations = cache.get(number)

    if locations:
        for location in locations:
            board_i, row_i, position_i = location
            grid[board_i][row_i][position_i] = -1

            if is_winner(grid, board_i, row_i, position_i):
                return (
                    grid,
                    sum(
                        [
                            (0 if grid[board_i][i][j] == -1 else grid[board_i][i][j])
                            for i in range(5)
                            for j in range(5)
                        ]
                    )
                    * number,
                )

    return (grid, None)


data = read_input()
numbers = parse_nums(data[0])

grid, cache = parse_grid(data[2:])
grid_ = grid

for number in numbers:
    grid, result = mark_numbers(grid, cache, number)

    if result:
        print(result)
        break
