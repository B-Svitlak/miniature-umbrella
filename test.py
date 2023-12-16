class Test:
    def __init__(self):
        self.a = 1
        self.b = 2

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


if __name__ == '__main__':
    t = Test()
    print(t.add())
    print(t.sub())