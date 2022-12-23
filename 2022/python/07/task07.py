from typing import List
import re

INPUT_FILE = "input.txt"


def ls(lines: List[str], idx: int) -> List[List[str]]:
    """Process dir listing."""
    listing = []
    for line in lines[idx:]:
        if "$" in line:
            break
        line_tmp = line.split(" ")
        line_tmp[1] = line_tmp[1][:-1]  # Remove \n
        listing.append(line_tmp)
    return listing


class TreeNode:
    def __init__(self, data, file_size: int, dir_or_file: str) -> None:
        self.data = data
        self.file_size = 0 if dir_or_file == "dir" else int(file_size)
        self.dir_or_file = dir_or_file
        self.children = {}
        self.parent = None

    def add_child(self, child) -> None:
        self.child = child
        child.parent = self
        self.children[child.data] = child

    def get_level(self) -> int:
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self) -> None:
        print('  '*self.get_level() + '|--', end='')
        print(f"{self.data} ({self.dir_or_file}, {self.file_size})")
        if self.children:
            for _, val in self.children.items():
                val.print_tree()

    def get_size(self) -> int:
        if self.dir_or_file == "file":
            return self.file_size
        else:
            if self.children:
                sum = 0
                for _, val in self.children.items():
                    sum += val.get_size()
                return sum
            else:
                return 0


all_dirs_size = []


def get_all_dirs_size(dir):
    all_dirs_size.append([dir.data, dir.dir_or_file, dir.get_size()])
    if dir.children:
        for _, val in dir.children.items():
            if val.dir_or_file == "dir":
                get_all_dirs_size(val)


def main():
    file = open(INPUT_FILE, "r")
    lines = file.readlines()
    root = TreeNode("/", file_size=0, dir_or_file="dir")

    for idx, line in enumerate(lines):
        cd_line = re.findall(r"\$ cd ([a-zA-Z]+|..|\/)", line)
        if cd_line:
            if cd_line[0] == "/":
                current_dir = root
            elif cd_line[0] == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.children[cd_line[0]]
        if line == "$ ls\n":
            listing = ls(lines, idx+1)
            for item in listing:
                if item[0] == "dir":
                    current_dir.add_child(TreeNode(
                        item[1], file_size=0, dir_or_file="dir"))
                else:
                    current_dir.add_child(TreeNode(
                        item[1], file_size=int(item[0]), dir_or_file="file"))

    root.print_tree()
    print(root.get_size())

    # Get dir sizes
    get_all_dirs_size(root)
    print(all_dirs_size)
    at_most_100000 = [dir for dir in all_dirs_size if dir[2] <= 100000]
    print(sum([dir[2] for dir in at_most_100000]))

    # Delete necessary space
    TOTAL_SPACE = 70000000
    NEEDED_SPACE = 30000000
    to_delete = NEEDED_SPACE - (TOTAL_SPACE - root.get_size())
    print(
        f"Root dir size: {root.get_size()}, needed space: {NEEDED_SPACE}, "
        f"to delete: {to_delete}"
    )
    to_delete_dir = ["aa", "dir", 100000000]
    for dir in all_dirs_size:
        if dir[2] >= to_delete:
            if dir[2] <= to_delete_dir[2]:
                to_delete_dir = dir
    print(f"Dir to delete: {to_delete_dir}")


if __name__ == "__main__":
    main()
