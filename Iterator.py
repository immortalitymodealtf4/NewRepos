class Iterator:
    """ Numeric iterator"""
    def __init__(self, some_iterables=0):
        self.some_iterables = some_iterables

    def __iter__(self):
        self.length = 0
        return self

    def __next__(self):
        if self.length < self.some_iterables:
            res = self.length
            self.length += 1
            return res
        else:
            raise StopIteration


class StrIterator:
    """ Iterator for string """
    def __init__(self, text=""):
        self.text = text
        self.str_length = len(self.text)
        self.char = self.text[self.str_length - 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.str_length > 0:
            res = self.char
            self.str_length -= 1
            self.char = self.text[self.str_length-1]
        else:
            raise StopIteration
        return res, self.str_length


str_iterator = StrIterator("Hello world")
str_iter = iter(str_iterator)
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))
print(next(str_iter))

num_iter = Iterator(8)
num_iterable = iter(num_iter)
print(next(num_iterable))
print(next(num_iterable))
print(next(num_iterable))
print(next(num_iterable))
print(next(num_iterable))
print(next(num_iterable))
print(next(num_iterable))
print(next(num_iterable))
print(next(num_iterable))