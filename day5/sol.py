import re


def parse_stacks(lines):
    for line_num, line in enumerate(lines):
        if "1" in line:
            num_cols = len(line.split())
            max_len = line_num
            break

    stacks = [[] for _ in range(num_cols)]
    for index in range(max_len-1, -1, -1):
        line = lines[index]
        for col_num in range(num_cols):
            char = line[col_num*4 + 1]
            if char != " ":
                stacks[col_num].append(char)

    return stacks


def parse_instructions(lines):
    pattern = r"move (\d*) from (\d*) to (\d*)"
    for line in lines:
        match = re.search(pattern, line)
        if match:
            yield match.group(1, 2, 3)


def process(instructions, stacks):
    new_stacks = [[val for val in s] for s in stacks]
    for count, frm, to in instructions:
        frm = int(frm) - 1
        to = int(to) - 1
        for _ in range(int(count)):
            new_stacks[to].append(new_stacks[frm].pop())
    return new_stacks


def process_part2(instructions, stacks):
    new_stacks = [[val for val in s] for s in stacks]
    for count, frm, to in instructions:
        frm = int(frm) - 1
        to = int(to) - 1
        to_move = [new_stacks[frm].pop() for _ in range(int(count))]
        new_stacks[to] += to_move[::-1]
    return new_stacks


if __name__ == '__main__':
    with open("input") as f:
        lines = list(f.read().splitlines())

    stacks = parse_stacks(lines)
    instructions = list(parse_instructions(lines))

    result = process(instructions, stacks)
    result_2 = process_part2(instructions, stacks)

    # Part 1
    print("".join(s[-1] for s in result))

    # Part 2
    print("".join(s[-1] for s in result_2))
