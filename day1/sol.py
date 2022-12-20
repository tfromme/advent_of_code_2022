def parse_lines(lines):
    start_slice, end_slice = 0, 0
    lines = list(lines)
    for line in lines:
        if line == "":
            yield lines[start_slice:end_slice]
            start_slice = end_slice + 1
        end_slice += 1

if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().split("\n")

    calories = parse_lines(int(line) if line else line for line in lines)
    sums = [sum(cals) for cals in calories]

    sums.sort(reverse=True)

    # Part 1
    print(sums[0])

    # Part 2
    print(sum(sums[0:3]))

