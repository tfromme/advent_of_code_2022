from functools import reduce

def batch(lst, n):
    l = len(lst)
    for ndx in range(0, l, n):
        yield lst[ndx:min(ndx + n, l)]


def get_badge(group):
    return reduce(lambda a, b: set(a) & set(b), group).pop()


def get_overlap(sack):
    comp1 = sack[:len(sack)//2]
    comp2 = sack[len(sack)//2:]

    return (set(comp1) & set(comp2)).pop()


def get_priority(item):
    o = ord(item)
    return o - 38 if o < 97 else o - 96

if __name__ == '__main__':
    with open("input") as f:
        sacks = f.read().splitlines()

    overlaps = [get_overlap(sack) for sack in sacks]
    priorities = [get_priority(item) for item in overlaps]

    groups = batch(sacks, 3)
    badges = [get_badge(group) for group in groups]
    badge_prios = [get_priority(badge) for badge in badges]

    # Part 1
    print(sum(priorities))

    # Part 2
    print(sum(badge_prios))
