import abc


class Node(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def name(self):
        pass


class Directory(Node):
    def __init__(self, dirname):
        self.dirname = dirname
        self._children = set()

    def name(self):
        for child in self._children:
            child.name()
        print(self.dirname)

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)


class File(Node):
    def __init__(self, filename):
        self.filename = filename

    def name(self):
        print(self.filename)


def main():
    dir = Directory('dir1')
    dir.add(File('file1'))
    dir.add(File('file2'))

    dir2 = Directory('dir2')
    dir2.add(File('file3'))
    dir.add(dir2)

    dir.name()


if __name__ == "__main__":
    main()