import os
import inspect


class Utils:
    @staticmethod
    def print_iterator(iterator):
        try:
            while True:
                print next(iterator),
        except StopIteration:
            pass


class Iterators(object):
    def basic_iterator_over_iterable(self):
        iterator = iter([i for i in xrange(10)])
        print 'Iteratable elements:',
        Utils.print_iterator(iterator)

    def lazy_iterator_vs_array(self):
        from itertools import repeat
        element_count = 10000
        lazy_iterator = repeat(1, times=element_count)

        import sys
        print '{}Size of lazy iterator = {} bytes vs size of array = {} bytes'.\
            format(os.linesep, sys.getsizeof(lazy_iterator), sys.getsizeof([1] * element_count))

    def test(self):
        self.basic_iterator_over_iterable()
        self.lazy_iterator_vs_array()


class CustomIterator(object):
    """"
    Iterator over an array
    """
    def __init__(self, iteratable=[]):
        self.iterator = iter(iteratable)

    def __iter__(self):
        return self

    def next(self):
        return self.iterator.next()

    @staticmethod
    def test():
        ci = CustomIterator([i for i in xrange(10)])
        print 'Custom iteration: ',
        Utils.print_iterator(ci)


class Counter(object):
    def __init__(self, start=0, direction=0):
        self.value = start
        self.direction = direction

    def __iter__(self):
        return self

    def next(self):
        if self.direction >= 0:
            value = self.value
            self.value += 1
            return value
        else:
            value = self.value
            self.value -= 1
            return value

    @staticmethod
    def test():
        counter = Counter(0, 0)
        print 'Counting upwards:',
        for _ in xrange(10):
            print next(counter),

        print '{}Counting downwards'.format(os.linesep),
        counter = Counter(start=counter.value, direction=-1)
        for _ in xrange(10):
            print next(counter),


class Generator(object):
    def generator_function(self):
        for i in xrange(10):
            yield i**2

    def generator_expression(self):
        return (i**2 for i in xrange(10))

    @staticmethod
    def test():
        g = Generator()
        print '{}Generator function elements: '.format(os.linesep),
        iterator = g.generator_function()
        Utils.print_iterator(iterator)

        print '{}Generator expression elements: '.format(os.linesep),
        iterator = g.generator_expression()
        Utils.print_iterator(iterator)


Iterators().test()
CustomIterator.test()
Counter.test()
Generator.test()


