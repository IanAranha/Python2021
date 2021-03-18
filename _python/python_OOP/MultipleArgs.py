# def varargs(arg1, *args):
#
#
#     print("Got " +arg1+ " and " +  ", ".join(args))
#
#
# varargs("one") # output: "Got one and "
# varargs("one", "two") # output: "Got one and two"
# varargs("one", "two", "three") # output: "Got one and two, three"

class MathDojo:
    def __init__(self):
        self.total = 0
        self.product = 1

    def add(self, *nums):
        for i in nums:
            print(i)
            self.total += i
        return self

    def subtract(self, *nums):
        for i in nums:
            print(i)
            self.total -= i
        return self

    def multiply(self, *nums):
        for i in nums:
            print(i)
            print(self.product)
            self.product = self.product * i
            print(self.product)
        return self.product

x = MathDojo()
print(x)
print(f"Total {x.total}")
x.add(3)
print(f"Total {x.total}")
x.add(1).add(2,3)
print(f"Total {x.total}")
x.subtract(9)
print(f"Total {x.total}")
x.add(1).add(2,3).add(4,5,6)
print(f"Total {x.total}")
y = MathDojo()
print(y)
y.multiply(2)
print(f"Product {y.product}")
y.multiply(1,2,3,4)
print(f"Product {y.product}")
