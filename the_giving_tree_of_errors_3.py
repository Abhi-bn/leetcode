class InvalidInputFormat(Exception):
    pass


class DuplicatePair(Exception):
    pass


class MoreChildren(Exception):
    pass


class MultipleRoot(Exception):
    pass


class CycleDetected(Exception):
    pass


class InvalidInput(Exception):
    pass


root = None


class Node:
    def __init__(self, val):
        self.val = val
        self.ch = []

    def add_child(self, child_val):
        if len(self.ch) == 2:
            raise MoreChildren()
        for c in self.ch:
            if c.val == child_val:
                raise DuplicatePair()

        self.ch.append(Node(child_val))
        visited = {}
        if Node.hasCycle(root, visited, root.val):
            raise CycleDetected()
        self.ch = sorted(self.ch, key=lambda x: x.val)

    def has_this_child(self, child_val):
        for c in self.ch:
            if c.val == child_val:
                return True
        return False

    @staticmethod
    def printLex(node):
        if node == None:
            return None
        print('('+node.val, end='')
        for c in node.ch:
            Node.printLex(c)
        print(')', end='')

    @staticmethod
    def get_parent(node, child_val):
        if node == None:
            return False
        if node.has_this_child(child_val):
            return True
        for c in node.ch:
            if Node.get_parent(c, child_val):
                return True
        return False

    @staticmethod
    def insert(node, parent_val, child_val):
        global root
        if root == None:
            node = Node(parent_val)
            root = node
            node.add_child(child_val)
            return True
        if node == None:
            return False
        if node.val == parent_val:
            node.add_child(child_val)
            return True
        for c in node.ch:
            if Node.insert(c, parent_val, child_val):
                return True
        return False

    @staticmethod
    def hasCycle(node, visited, parent):
        visited[node.val] = True
        for c in node.ch:
            visited.setdefault(c.val, False)
            if not visited[c.val]:
                if Node.hasCycle(c, visited, node.val):
                    return True
            elif c != parent:
                return True
        return False


def get_valid_input():
    getnodes = input()
    cleaned = []
    pair_node = getnodes.split(' ')
    # checking for trailing and leading whitespaces and empty
    if getnodes.endswith(' ') or getnodes.startswith(' '):
        raise InvalidInput()
    for s in pair_node:
        pair = []
        # checking for valid (parent, child)
        if s.find('(') == -1 or s.find(')') == -1 or s.find('(') or s.find(',') == -1 > s.find(',') > s.find(')'):
            raise InvalidInput()
        splits = s.split(',')
        if len(splits) != 2:
            raise InvalidInput()
        first, second = splits
        first = first[first.find('(') + 1:]
        second = second[:second.find(')')]
        # should only have single uppercase letter
        if len(first) != 1 or len(second) != 1 or not first.isupper() or not second.isupper():
            raise InvalidInput()
        cleaned.append([first, second])
    return cleaned
# Enter your code here. Read input from STDIN. Print output to STDOUT


def main():
    try:
        all_list = get_valid_input()
        for parent, child in all_list:
            inserted = Node.insert(root, parent, child)
            if inserted:
                continue
            raise MultipleRoot()
        Node.printLex(root)
    except InvalidInput:
        print('E1')
    except DuplicatePair:
        print('E2')
    except MoreChildren:
        print('E3')
    except MultipleRoot:
        print('E4')
    except CycleDetected:
        print('E5')


main()
