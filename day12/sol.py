from queue import SimpleQueue
from typing import Callable, Iterable, List, Optional, Tuple

Board = List[List[int]]
Pos = Tuple[int, int]


def parse_lines(lines: Iterable[str]) -> Tuple[Board, Pos, Pos]:
    starting_pos = None
    ending_pos = None

    def parse_char(char: str, x: int, y: int) -> int:
        nonlocal starting_pos, ending_pos
        if char == "S":
            starting_pos = x, y
            return 1
        if char == "E":
            ending_pos = x, y
            return 26
        return ord(char) - 96

    return [
        [parse_char(char, x, y) for y, char in enumerate(line)]
        for x, line in enumerate(lines)
    ], starting_pos, ending_pos


def is_valid(board: Board, pos: Pos) -> bool:
    if pos[0] < 0 or pos[1] < 0:
        return False
    try:
        board[pos[0]][pos[1]]
    except IndexError:
        return False
    return True


def valid_neighbors(board: Board, pos: Pos) -> Iterable[Pos]:
    pos_x, pos_y = pos
    all_neighbors = (
        (pos_x - 1, pos_y),
        (pos_x + 1, pos_y),
        (pos_x, pos_y - 1),
        (pos_x, pos_y + 1),
    )
    for x, y in all_neighbors:
        if is_valid(board, (x, y)):
            if board[x][y] - board[pos_x][pos_y] <= 1:
                yield x, y


def traverse_board(
    board: Board,
    starting_pos: Pos,
    ending_pos: Pos,
) -> Optional[int]:
    locations_to_traverse = SimpleQueue()
    locations_to_traverse.put((starting_pos, 0))

    seen = set()

    while not locations_to_traverse.empty():
        pos, distance = locations_to_traverse.get()
        if pos == ending_pos:
            return distance

        for neighbor in valid_neighbors(board, pos):
            if neighbor not in seen:
                seen.add(neighbor)
                locations_to_traverse.put((neighbor, distance + 1))

    return None


def main(input_path="input"):
    with open(input_path) as f:
        lines = f.read().splitlines()

    board, starting_pos, ending_pos = parse_lines(lines)

    part1 = traverse_board(board, starting_pos, ending_pos)

    min_path_len = float("inf")
    for x, line in enumerate(board):
        for y, elevation in enumerate(line):
            if elevation == 1:
                path_len = traverse_board(board, (x, y), ending_pos)
                if path_len is not None:
                    min_path_len = min(path_len, min_path_len)

    part2 = min_path_len

    return part1, part2


if __name__ == '__main__':
    print(main())
