from functools import reduce

def is_touching(head_pos, tail_pos):
    return (abs(head_pos[0] - tail_pos[0]) <= 1 and
            abs(head_pos[1] - tail_pos[1]) <= 1)


def new_tail_pos(head_pos, tail_pos):
    if is_touching(head_pos, tail_pos):
        return tail_pos

    xdiff = abs(head_pos[0] - tail_pos[0])
    ydiff = abs(head_pos[1] - tail_pos[1])

    if ydiff > xdiff:
        x = head_pos[0]
    else:
        x = head_pos[0] - 1 if (head_pos[0] - tail_pos[0]) > 0 else head_pos[0] + 1

    if xdiff > ydiff:
        y = head_pos[1]
    else:
        y = head_pos[1] - 1 if (head_pos[1] - tail_pos[1]) > 0 else head_pos[1] + 1

    return x, y


def move_head(head_pos, direction):
    if direction == 'R':
        head_pos = (head_pos[0] + 1, head_pos[1])
    elif direction == 'L':
        head_pos = (head_pos[0] - 1, head_pos[1])
    elif direction == 'U':
        head_pos = (head_pos[0], head_pos[1] + 1)
    elif direction == 'D':
        head_pos = (head_pos[0], head_pos[1] - 1)
    return head_pos


def simulate_line(line, positions):
    all_tail_pos = {positions[-1]}
    direction, count = line
    for _ in range(count):
        positions[0] = move_head(positions[0], direction)
        for i in range(len(positions) - 1):
            positions[i+1] = new_tail_pos(positions[i], positions[i+1])
        all_tail_pos.add(positions[-1])

    return all_tail_pos


def simulate(lines, start, num_knots=2):
    positions = [start] * num_knots
    return reduce(
        lambda posns, line: posns | simulate_line(line, positions),
        lines,
        set(),
    )



if __name__ == '__main__':
    with open("input") as f:
        lines = [(line.split()[0], int(line.split()[1])) for line in f.read().splitlines()]

    start = 0, 0
    tail_positions = simulate(lines, start, 2)
    ten_tail_positions = simulate(lines, start, 10)


    # Part 1
    print(len(tail_positions))

    # Part 2
    print(len(ten_tail_positions))
