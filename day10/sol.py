def calculate_cycles(lines):
    register = 1

    for line in lines:
        if line.startswith("noop"):
            yield register
        elif line.startswith("addx"):
            increment = int(line.split()[1])
            yield register
            yield register
            register += increment


def render_image(cycles) -> str:
    str = ""
    for i, register in enumerate(cycles):
        horizontal_position = i % 40

        sprite_shape = (register - 1, register, register + 1)

        str += "#" if horizontal_position in sprite_shape else "."
        if horizontal_position == 39:
            str += "\n"
    return str


def main(input_path="input"):
    with open(input_path) as f:
        lines = f.read().splitlines()

    cycles = list(calculate_cycles(lines))

    valid_cycles = (20, 60, 100, 140, 180, 220)

    strengths = [(i + 1) * cycle for i, cycle in enumerate(cycles) if i + 1 in valid_cycles]

    part1 = sum(strengths)
    part2 = render_image(cycles)

    return part1, part2


if __name__ == '__main__':
    print(main())
