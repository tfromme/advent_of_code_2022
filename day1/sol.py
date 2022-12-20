def parse_lines(lines):
    start_slice, end_slice = 0, 0
    lines = list(lines)
    for line in lines:
        if line == "":
            yield lines[start_slice:end_slice]
            start_slice = end_slice + 1
        end_slice += 1


def main(input_path="input"):
    with open(input_path) as f:
        lines = f.read().split("\n")

    calories = parse_lines(int(line) if line else line for line in lines)
    sums = [sum(cals) for cals in calories]

    sums.sort(reverse=True)

    part1 = sums[0]
    part2 = sum(sums[0:3])

    return part1, part2


if __name__ == "__main__":
    print(main())
