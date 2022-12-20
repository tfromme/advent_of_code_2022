def calc_part2_points(rnd):
    shape = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2,
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3,
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1,
        },
    }
    output = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }
    them, me = rnd
    return shape[them][me] + output[me]


def calc_points(rnd):
    output = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0,
        },
        "B": {
            "X": 0,
            "Y": 3,
            "Z": 6,
        },
        "C": {
            "X": 6,
            "Y": 0,
            "Z": 3,
        },
    }
    shape = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    them, me = rnd
    return shape[me] + output[them][me]


def main(input_path="input"):
    with open(input_path) as f:
        guide = [line.split(" ") for line in f.read().split("\n")][:-1]

    part1_rounds = [calc_points(line) for line in guide]
    part2_rounds = [calc_part2_points(line) for line in guide]

    part1 = sum(part1_rounds)
    part2 = sum(part2_rounds)

    return part1, part2


if __name__ == '__main__':
    print(main())
