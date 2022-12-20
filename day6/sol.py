
def locate_start(line):
    for i in range(4, len(line) + 1):
        sub = line[i-4:i]
        if len(set(sub)) == 4:
            return i


if __name__ == '__main__':
    with open("test_input") as f:
        lines = f.read().splitlines()

    starts = map(locate_start, lines)

    # Part 1
    print(list(starts))

    # Part 2
