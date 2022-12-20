def transpose(lines):
    return [
        [line[i] for line in lines]
        for i in range(len(lines[0]))
    ]


def horizontal_visible_mask(lines):
    for line in lines:
        tallest_so_far = -1
        left_mask = []
        for val in line:
            left_mask.append(val > tallest_so_far)
            if val > tallest_so_far:
                tallest_so_far = val

        tallest_so_far = -1
        right_mask = []
        for val in line[::-1]:
            right_mask.append(val > tallest_so_far)
            if val > tallest_so_far:
                tallest_so_far = val
        right_mask = right_mask[::-1]

        yield [l or r for (l, r) in zip(left_mask, right_mask)]


def combine_masks(mask1, mask2):
    for l1, l2 in zip(mask1, mask2):
        yield [val1 or val2 for (val1, val2) in zip(l1, l2)]


def horizontal_score(lines):
    for line in lines:
        left_scores = []
        for i, val in enumerate(line):
            left_score = 0
            for j in range(i - 1, -1, -1):
                left_score += 1
                if line[j] >= val:
                    break
            left_scores.append(left_score)

        right_scores = []
        for i, val in enumerate(line):
            right_score = 0
            for j in range(i + 1, len(line)):
                right_score += 1
                if line[j] >= val:
                    break
            right_scores.append(right_score)

        yield [left * right for left, right in zip(left_scores, right_scores)]


def combine_scores(scores1, scores2):
    for l1, l2 in zip(scores1, scores2):
        yield [val1 * val2 for (val1, val2) in zip(l1, l2)]


def main(input_path="input"):
    with open(input_path) as f:
        lines = [[int(val) for val in line] for line in f.read().splitlines()]

    horizontal = list(horizontal_visible_mask(lines))
    transposed = transpose(lines)
    vertical = list(horizontal_visible_mask(transposed))

    mask = list(combine_masks(horizontal, transpose(vertical)))

    part1 = sum(sum(1 if val else 0 for val in line) for line in mask)

    horizontal_scores = list(horizontal_score(lines))
    vertical_scores = list(horizontal_score(transposed))

    scores = list(combine_scores(horizontal_scores, transpose(vertical_scores)))

    part2 = max(max(line) for line in scores)

    return part1, part2


if __name__ == '__main__':
    print(main())
