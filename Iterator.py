class Iterator:

    def __init__(self, some_iterables = 0):
        self.some_iterables = some_iterables

    def __iter__(self):
        self.length = 0
        return self

    def __next__(self):
        if self.length <= self.some_iterables:
            res = self.length
            self.length += 1
            print(res)
            return res
        else:
            raise StopIteration


new_iter = Iterator(4)
i = iter(new_iter)
next(i)
next(i)
next(i)
next(i)
next(i)
next(i)