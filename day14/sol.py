import itertools
from typing import Iterable, List, Tuple


Point = Tuple[int, int]


def pairwise(iterable: Iterable):
    """From itertools, not implemented until 3.10"""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def line_from_points(point1: Point, point2: Point) -> Iterable[Point]:
    if point1[0] == point2[0]:
        x = point1[0]
        min_y = min(point1[1], point2[1])
        max_y = max(point1[1], point2[1])
        for y in range(min_y, max_y + 1):
            yield x, y
    elif point1[1] == point2[1]:
        y = point1[1]
        min_x = min(point1[0], point2[0])
        max_x = max(point1[0], point2[0])
        for x in range(min_x, max_x + 1):
            yield x, y
    else:
        raise NotImplementedError("line_from_points() only supports straight lines")


class Board:
    def __init__(self, point_lists: Iterable[List[Point]], floor=False):
        point_lists = list(point_lists)
        # TODO: Dynamically scale this param
        self.min_x = min(point[0] for pl in point_lists for point in pl) - 200
        self.max_x = max(point[0] for pl in point_lists for point in pl) + 200
        self.min_y = 0
        self.max_y = max(point[1] for pl in point_lists for point in pl) + 2

        assert self.min_x <= 500 <= self.max_x
        
        x_size = self.max_x - self.min_x + 1
        y_size = self.max_y - self.min_y + 1

        self.start_point = 500, 0

        self.board = [["." for _ in range(x_size)] for _ in range(y_size)]
        if floor:
            self.board[-1] = ["#" for _ in range(x_size)]

        for point_list in point_lists:
            for p1, p2 in pairwise(point_list):
                for point in line_from_points(p1, p2):
                    self[point] = "#"

        self[self.start_point] = "S"


    def drop_sand(self):
        x, y = self.start_point
        if self[x, y] == "o":
            return False

        while True:
            if y >= self.max_y:
                return False

            if self[x, y + 1] == ".":
                y += 1
            elif self[x - 1, y + 1] == ".":
                x -= 1
                y += 1
            elif self[x + 1, y + 1] == ".":
                x += 1
                y += 1
            else:
                self[x, y] = "o"
                return True


    def __getitem__(self, point: Point):
        x, y = point
        return self.board[y - self.min_y][x - self.min_x]

    def __setitem__(self, point: Point, value: str):
        x, y = point
        self.board[y - self.min_y][x - self.min_x] = value

    def __str__(self):
        return "\n".join("".join(line) for line in self.board)


def str_to_point(string: str) -> Point:
    x, y = string.strip().split(",")
    return int(x), int(y)


def parse_lines(lines: Iterable[str]) -> Iterable[List[Point]]:
    for line in lines:
        point_strs = line.split("->")
        yield list(map(str_to_point, point_strs))


def main(input_path="input"):
    with open(input_path) as f:
        lines = f.read().splitlines()

    point_lists = list(parse_lines(lines))

    board1 = Board(point_lists)
    part1 = 0
    while board1.drop_sand():
        part1 += 1

    board2 = Board(point_lists, floor=True)
    part2 = 0
    while board2.drop_sand():
        part2 += 1

    return part1, part2


if __name__ == '__main__':
    print(main())
