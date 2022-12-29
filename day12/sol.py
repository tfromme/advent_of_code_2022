from typing import Callable, Iterable, List


def parse_char(char: str) -> int:
    return ord(char) - 96


def parse_lines(lines: Iterable[str]) -> List[List[int]]:
    starting_pos = None
    ending_pos = None

    def parse_char(char: str, x: int, y: int) -> int:
        if char == "S":
            starting_pos = x, y
            return 1
        if char == "E":
            ending_pos = x, y
            return 26
        return ord(char) - 96

    return [[parse_char(char) for char in line] for line in lines], starting_pos, ending_pos


def main(input_path="input"):
    with open(input_path) as f:
        lines = f.read().splitlines()

    board, starting_pos, ending_pos = parse_lines(lines)

    print(board, starting_pos, ending_pos)

    part1 = None
    part2 = None

    return part1, part2


if __name__ == '__main__':
    print(main())
