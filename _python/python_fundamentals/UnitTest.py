import unittest  # Python Testing Framework


#The unit we will run a test on.
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False



#Unit Tests
class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(isEven(3), True)
        # another way to write above is
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(2), False)
        # another way to write above is
        self.assertFalse(isEven(3))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests
