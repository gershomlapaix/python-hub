class Node():
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n
        # self.prev_node = p

    def __str__(self):
        return ('('+str(self.data)+')')


class LinkedList():

    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def find(self, d) -> None:
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node
        return None

    def remove(self, d):
        this_node = self.root
        prev_node = None
        
        while this_node is not None:
            if this_node.data == d:
                this_node =
