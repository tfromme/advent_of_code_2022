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


def render_image(cycles):
    for i, register in enumerate(cycles):
        horizontal_position = i % 40

        sprite_shape = (register - 1, register, register + 1)

        char = "#" if horizontal_position in sprite_shape else "."
        end = "\n" if horizontal_position == 39 else ""

        print(char, end=end)


if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines()

    cycles = list(calculate_cycles(lines))

    valid_cycles = (20, 60, 100, 140, 180, 220)

    strengths = [(i+1) * cycle for i, cycle in enumerate(cycles) if i+1 in valid_cycles]

    # Part 1
    print(sum(strengths))

    # Part 2
    render_image(cycles)
