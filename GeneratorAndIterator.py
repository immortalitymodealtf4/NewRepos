class Iterator:

    def __init__(self, max_pow=0):
        self.max_pow = max_pow

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max_pow:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration


def generator(max_pow):
    n = 0
    while n < max_pow:
        yield n ** 2
        n += 1

