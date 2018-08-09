class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        pass

    def __contains__(self, data):
        """
        implements the in operator
        """
        if self.head is not None:
            current = self.head
            while True:
                if current.data == data:
                    return True  # value found in list

                current = current.next
                if current == self.head:
                    break

        return False

    def __iter__(self):
        return self

    def next(self):
        current = self.head
        while current.next != self.head:
            yield current.data


class CircularLinkedListNoSentinel(CircularLinkedList):
    def __init__(self):
        self.head = None

    def push(self, data):
        n = Node(data)
        n.next = self.head

        current = self.head
        if self.head is not None:
            while current.next != self.head:
                current = current.next
            current.next = n
        else:
            n.next = n
            self.head = n

    def reverse(self):
        if self.head is not None:
            current = self.head
            while current.next != self.head:
                current = current.next

            prev = current
            current = self.head

            while True:
                _next = current.next
                current.next = prev
                prev = current
                current = _next
                if current == self.head:
                    break

    def delete_the_other_nth_element(self, n):
        """"
        Deletes each nth element from the list
        """
        if self.head is not None:
            current = self.head

            while True:
                _next = current

                # iterate n elements, if header is encountered abort
                for _ in range(n):
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


class CircularLinkedListWithSentinel(CircularLinkedList):
    def __init__(self):
        self.head = Node(None)      # this is the sentinel node
        self.head.next = self.head

    def push_front(self, data):
        n = Node(data)
        n.next = self.head.next
        self.head.next = n

    def push_end(self, data):
        n = Node(data)
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


c1 = CircularLinkedListWithSentinel()
for i in range(10):
    c1.push_front(i)
c1.list()

c2 = CircularLinkedListWithSentinel()
for i in range(10):
    c2.push_end(i)
c2.list()

c3 = CircularLinkedListNoSentinel()
for i in range(10):
    c3.push(i)
c3.list()
print '\nReversing no-sentinel list...'
c3.reverse()
c3.list()

print '\nDeleting the other element...'
c3.delete_the_other_nth_element(1)
c3.list()
