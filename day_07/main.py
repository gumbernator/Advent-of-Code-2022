
from typing import Dict, List


class Directory:
    def __init__(self, name: str, files: Dict[str, int], dirs: Dict[str, "Directory"]):
        self.name = name
        self.files = files
        self.dirs = dirs
        self.islisted = False
        self.total_size = None

    def get_size(self) -> int:
        if self.total_size is not None:
            return self.total_size
        files_size = sum(list(self.files.values()))
        dirs_size = 0
        for name in self.dirs:
            if name == '..': continue
            dirs_size += self.dirs[name].get_size()
        self.total_size = files_size + dirs_size
        return self.total_size

    def __repr__(self):
        return f'{self.name}=files: {self.files}, dirs: {self.dirs}'


def part1(lines: List[str]):
    root = Directory('/', {}, {})
    current_dir = root
    i = 0
    while i < len(lines):
        if lines[i].startswith('$ ls'):
            if not current_dir.islisted:
                i += 1
                while i < len(lines) and not lines[i].startswith('$'):
                    if lines[i].startswith('dir'):
                        name = lines[i].split('dir ')[1]
                        current_dir.dirs[name] = Directory(name, {}, {'..': current_dir})
                    else:
                        splits = lines[i].split(' ')
                        size, name = int(splits[0]), splits[1]
                        current_dir.files[name] = size
                    i += 1
                current_dir.islisted = True
        elif lines[i].startswith('$ cd /'):
            current_dir = root
            i += 1
        elif lines[i].startswith('$ cd '):
            changing_dir = lines[i].split('$ cd ')[1]
            current_dir = current_dir.dirs[changing_dir]
            i += 1
    # print(root)
    dir_sizes = []
    def walk(root_dir: Directory):
        dir_sizes.append(root_dir.get_size())
        for name, dir in root_dir.dirs.items():
            if name == '..': continue
            walk(dir)
    walk(root)
    # print(dir_sizes)
    print('part1:', sum([dir_size for dir_size in dir_sizes if dir_size <= 100000]))


def part2(lines: List[str]):
    root = Directory('/', {}, {})
    current_dir = root
    i = 0
    while i < len(lines):
        if lines[i].startswith('$ ls'):
            if not current_dir.islisted:
                i += 1
                while i < len(lines) and not lines[i].startswith('$'):
                    if lines[i].startswith('dir'):
                        name = lines[i].split('dir ')[1]
                        current_dir.dirs[name] = Directory(name, {}, {'..': current_dir})
                    else:
                        splits = lines[i].split(' ')
                        size, name = int(splits[0]), splits[1]
                        current_dir.files[name] = size
                    i += 1
                current_dir.islisted = True
        elif lines[i].startswith('$ cd /'):
            current_dir = root
            i += 1
        elif lines[i].startswith('$ cd '):
            changing_dir = lines[i].split('$ cd ')[1]
            current_dir = current_dir.dirs[changing_dir]
            i += 1
    # print(root)
    dir_sizes = []
    def walk(root_dir: Directory):
        dir_sizes.append(root_dir.get_size())
        for name, dir in root_dir.dirs.items():
            if name == '..': continue
            walk(dir)
    walk(root)
    total_space = 70_000_000
    required_space = 30_000_000
    unused_space = total_space - root.get_size()
    for dir_size in sorted(dir_sizes):
        if unused_space + dir_size >= required_space:
            print('part2:', dir_size)
            return
    print('part2:', 'not found')

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.replace('\n', '') for line in lines]
        part1(lines)
        part2(lines)
