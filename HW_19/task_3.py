class MyIter:
    def __init__(self, obj: iter):
        self.obj = obj
        self.index = 0
        self.obj = list(self.obj)

    def next(self):
        if len(self.obj) - 1 >= self.index:
            yield self.obj[self.index]
            self.index += 1