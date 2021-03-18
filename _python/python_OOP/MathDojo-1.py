class MathDojo:
    def __init__(self):
        self.total = 0

    def add(self, *args):
        for i in args:
            self.total += i
        return self

    def subtract(self, *args):
        for i in args:
            self.total -= i
        return self

    def result(self):
        print("Answer is {}".format(self.total))

x = MathDojo().add(2).add(2,5).result()
y=MathDojo().subtract(3,2).result()
z=MathDojo().add(2).add(2,5,1).subtract(3,2).result()
