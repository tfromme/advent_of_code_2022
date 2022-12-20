from functools import reduce


def batch(lst, n):
    length = len(lst)
    for ndx in range(0, length, n):
        yield lst[ndx:min(ndx + n, length)]


def get_badge(group):
    return reduce(lambda a, b: set(a) & set(b), group).pop()


def get_overlap(sack):
    comp1 = sack[:len(sack) // 2]
    comp2 = sack[len(sack) // 2:]

    return (set(comp1) & set(comp2)).pop()


def get_priority(item):
    o = ord(item)
    return o - 38 if o < 97 else o - 96


def main(input_path="input"):
    with open(input_path) as f:
        sacks = f.read().splitlines()

    overlaps = [get_overlap(sack) for sack in sacks]
    priorities = [get_priority(item) for item in overlaps]

    groups = batch(sacks, 3)
    badges = [get_badge(group) for group in groups]
    badge_prios = [get_priority(badge) for badge in badges]

    part1 = sum(priorities)
    part2 = sum(badge_prios)

    return part1, part2


if __name__ == '__main__':
    print(main())
