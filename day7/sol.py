ALL_DIRECTORIES = []


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = int(size)
        self.parent = parent

    def __str__(self):
        return f"- {self.name} (file, size={self.size})"


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent

    def find_child(self, name):
        for c in self.children:
            if c.name == name:
                return c
        new_child = Directory(name, self)
        self.children.append(new_child)
        ALL_DIRECTORIES.append(new_child)
        return new_child

    @property
    def size(self):
        return sum(c.size for c in self.children)

    def __str__(self):
        print(self.name, [c.name for c in self.children])
        child_strs = "\n".join(f"  {child}" for child in self.children)
        return f"- {self.name} (dir)\n" + child_strs


def parse_lines(lines):
    root = Directory("/")
    current_node = root
    ALL_DIRECTORIES.append(root)
    for line in lines:
        if line.startswith("$"):
            if "cd" in line:
                dirname = line.split()[2]
                if dirname == "/":
                    current_node = root
                elif dirname == "..":
                    current_node = current_node.parent
                else:
                    current_node = current_node.find_child(dirname)
        else:
            if line.startswith("dir"):
                dirname = line.split()[1]
                current_node.find_child(dirname)
            else:
                file_size, file_name = line.split()
                file = File(file_name, file_size, current_node)
                current_node.children.append(file)
    return root



if __name__ == '__main__':
    with open("input") as f:
        lines = f.read().splitlines()

    tree = parse_lines(lines)

    filtered_dirs = [d for d in ALL_DIRECTORIES if d.size <= 100000]

    min_to_delete = 30000000 - (70000000 - tree.size)

    to_delete = tree
    for d in ALL_DIRECTORIES:
        if d.size > min_to_delete and d.size < to_delete.size:
            to_delete = d

    # Part 1
    print(sum(d.size for d in filtered_dirs))

    # Part 2
    print(to_delete.size)
