import unittest

class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("I will run once before every test")

    def test_method_1(self):
        print("Running method 1")

    def test_method_2(self):
        print("Running method 2")

    def tearDown(self):
        print("I will run after every test")

if __name__== '__main__':
    unittest.main(verbosity=2)
