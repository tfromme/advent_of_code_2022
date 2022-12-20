
def locate_start(line):
    for i in range(4, len(line) + 1):
        sub = line[i - 4:i]
        if len(set(sub)) == 4:
            return i


def main(input_path="input"):
    with open(input_path) as f:
        lines = f.read().splitlines()

    starts = map(locate_start, lines)

    part1 = list(starts)
    part2 = None  # WTF

    return part1, part2


if __name__ == '__main__':
    print(main())
