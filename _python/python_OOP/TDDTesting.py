import unittest  # Python Testing Framework

from ReverseList import reverseList
from IsPallindrome import isPallindrome
from Coins import coins
from Factorial import factorial
from Fibonacci import fib

# def reverseList(list):
#     mid = int(len(list)/2)
#     for i in range(0, mid):
#         print("Swapping", list[i], list[len(list)-1-i])
#         list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
#     return list


#Unit Tests
class ReverseList(unittest.TestCase):
    # each method in this class is a test to be run
    def test1(self):
        self.assertEqual(reverseList([1,2,3,4]), [4,3,2,1])
    def test2(self):
        self.assertEqual(reverseList([-2,3,5,-9,7]),[7,-9,5,3,-2])
    #     # another way to write above is
    #     self.assertFalse(isEven(3))
    # # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")

class IsPallindrome(unittest.TestCase):
    def test1(self):
        return self.assertEqual(isPallindrome("racecar"), True)
    def test2(self):
        return self.assertEqual(isPallindrome("rabbit"),False)

class Coins(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coins(93), [3,1,1,3])
        
    def test2(self):
        return self.assertEqual(coins(66), [2,1,1,1])
    
    def test3(self):
        return self.assertEqual(coins(37), [1,1,0,2])
    
    def test4(self):
        return self.assertEqual(coins(10), [0,1,0,0])

class Factorial(unittest.TestCase):
    def test1(self):
        return self.assertEqual(factorial(10), 3628800)
    def test2(self):
        return self.assertEqual(factorial(1), 1)
    def test3(self):
        return self.assertEqual(factorial(2), 2)


class Fibonnaci(unittest.TestCase):
    def test1(self):
        return self.assertEqual(fib(7), 13)
if __name__ == '__main__':
    unittest.main() # this runs our tests
