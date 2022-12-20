def parse_lines(lines):
    for line in lines:
        r1, r2 = line.split(",")
        a, b = r1.split("-")
        c, d = r2.split("-")
        yield [(int(a), int(b)), (int(c), int(d))]


def contains(pair):
    r1, r2 = pair
    r1_contains_r2 = r1[0] <= r2[0] and r1[1] >= r2[1]
    r2_contains_r1 = r2[0] <= r1[0] and r2[1] >= r1[1]
    return r1_contains_r2 or r2_contains_r1


def overlaps(pair):
    r1, r2 = pair
    a = r2[0] <= r1[0] <= r2[1]
    b = r2[0] <= r1[1] <= r2[1]
    c = r1[0] <= r2[0] <= r1[1]
    d = r1[0] <= r2[1] <= r1[1]
    return a or b or c or d


if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines()

    pairs = list(parse_lines(lines))
    contains = [contains(pair) for pair in pairs]
    overlaps = [overlaps(pair) for pair in pairs]

    # Part 1
    print(len([c for c in contains if c]))

    # Part 2
    print(len([o for o in overlaps if o]))
