import os
from collections import deque


class Node(object):
    """
    Implements a generic data structure node
    """
    def __init__(self, data):
        self.data = data


class SimpleLinkedListNode(Node):
    """
    Implements a simple linked list node
    """
    def __init__(self, data):
        super(SimpleLinkedListNode, self).__init__(data)
        self.next = None


class DoubleLinkedListNode(Node):
    """
    Implements a double linked list node
    """
    def __init__(self, data):
        super(DoubleLinkedListNode, self).__init__(data)
        self.next = None
        self.prev = None


class TreeNode(Node):
    """
    Implements a generic tree node
    """
    def __init__(self, data):
        super(TreeNode, self).__init__(data)
        self.parent = None
        self.children = []

    def add_children(self, values):
        for v in values:
            child = TreeNode(v)
            child.parent = self
            self.children.append(child)


class SimpleCircularLinkedList(object):
    """
    Implements an generic simple circular linked list
    """
    def __contains__(self, data):
        """
        implements the `in` operator
        """
        if self.head is not None:
            if self.head.data == data:
                return True

            current = self.head
            while current.next != self.head:
                if current.data == data:
                    return True  # value found in list

                current = current.next

        return False

    def __iter__(self):
        return self

    def get(self):
        # generator with lazy retrieval of the list elements
        current = self.head
        while current.next != self.head:
            yield current.data
            current = current.next


class SimpleCircularLinkedListNoSentinel(SimpleCircularLinkedList):
    """"
    Implements a circular simple linked list with no sentinel node (i.e. its first node is also its head)
    """
    def __init__(self):
        self.head = None  # new list is always created empty

    def insert_before(self, data, node):
        """
        Insert a node before a given node
        :param data: Inserted node data
        :param node: Node before which to insert the new node
        """
        # in case list is empty, do nothing

        if self.head is not None:
            new_node = SimpleLinkedListNode(data)  # create the new node using given data
            new_node.next = node  # new node points to node it's inserted before

            # seek the node after the node to be inserted before
            current = self.head
            while current.next != node:
                current = current.next
            current.next = new_node  # after node points to the newly created node

    def insert_after(self, data, node):
        """
        Insert a node after a given node
        :param data: Inserted node data
        :param node: Node after which to insert the new node
        """
        # in case list is empty, do nothing

        if self.head is not None:
            new_node = SimpleLinkedListNode(data)  # create the new node using given data
            new_node.next = node.next  # new node points to node's next
            node.next = new_node  # existing node points to the newly created node

    def append(self, data):
        """
        Adds a new element at the end of the list (i.e. before the head, if any)
        """
        n = SimpleLinkedListNode(data)  # create the new node with the given data

        if self.head is not None:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = n  # the last node in the list will point to the newly added node
        else:
            self.head = n  # list was empty, new node becomes the head

        n.next = self.head  # newly added node always points to the head

    def reverse(self):
        """
        Reverse a simple circular linked list, by changing the direction of the node links
        """
        if self.head is not None:
            current = self.head

            # seek the node before the head
            while current.next != self.head:
                current = current.next

            prev = current
            current = self.head

            while True:
                _next = current.next
                current.next = prev
                prev = current
                current = _next
                if current == self.head:  # head is reached, list is fully reversed
                    break

    def delete_each_nth_element(self, step):
        """
        Deletes each nth element from the list
        :param step: Indicates the step of deletion
        """
        if self.head is not None:
            current = self.head

            while True:
                _next = current

                # iterate `step` elements, if header is encountered abort
                for _ in range(step):
                    _next = _next.next
                    if _next == self.head:
                        return

                current.next = _next.next
                current = current.next

                if current == self.head:
                    return

    def list(self):
        print '\nLinked list w/o sentinel:',
        if self.head is not None:
            current = self.head
            while True:
                print "{}->".format("head({})".format(current.data) if current == self.head else current.data),
                current = current.next
                if current == self.head:
                    print "head({})".format(current.data)
                    break

    @staticmethod
    def test():
        c3 = SimpleCircularLinkedListNoSentinel()
        for i in range(10):
            c3.append(i)
        c3.list()
        print '\nReversing no-sentinel list...'
        c3.reverse()
        c3.list()

        print '\nDeleting the other 2nd element...',
        c3.delete_each_nth_element(2)
        c3.list()

        items_generator = c3.get()
        try:
            print 'Printing items in a lazy mode: ',
            while True:
                print next(items_generator),
        except StopIteration:
            pass


class SimpleCircularLinkedListWithSentinel(SimpleCircularLinkedList):
    def __init__(self):
        self.head = SimpleLinkedListNode(None)  # this is the sentinel node
        self.head.next = self.head

    def add_in_front(self, data):
        n = SimpleLinkedListNode(data)
        n.next = self.head.next
        self.head.next = n

    def add_to_end(self, data):
        n = SimpleLinkedListNode(data)
        n.next = self.head

        '''position to the last element before head(i.e. tail)'''
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = n

    def list(self):
        print '\nLinked list with sentinel:',

        current = self.head
        while True:
            print "{}->".format("head({})".format(current.data) if current.data is None else current.data),
            current = current.next
            if current == self.head:
                print "head({})".format(current.data)
                break

    @staticmethod
    def test():
        c1 = SimpleCircularLinkedListWithSentinel()
        for _ in xrange(10):
            c1.add_in_front(_)
        c1.list()

        c2 = SimpleCircularLinkedListWithSentinel()
        for _ in xrange(10):
            c2.add_to_end(_)
        c2.list()


class Tree(object):
    """
    Implements a generic tree structure
    """
    def __init__(self, data):
        self.root = TreeNode(data)

    def traverse_dfs(self, root):
        if root is None:
            return

        print root.data,

        for child in root.children:
            self.traverse_dfs(root=child)

    def traverse_bfs(self, root):
        queue = deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()
            print curr.data,
            for child in curr.children:
                queue.append(child)

    @staticmethod
    def test():
        tree = Tree(1)
        tree.root.add_children([2, 3])
        tree.root.children[0].add_children([4, 5])
        tree.root.children[1].add_children([6])
        print 'Traverse DFS:',
        tree.traverse_dfs(tree.root)

        print os.linesep + 'Traverse BFS:',
        tree.traverse_bfs(tree.root)


SimpleCircularLinkedListWithSentinel.test()
SimpleCircularLinkedListNoSentinel.test()
Tree.test()
