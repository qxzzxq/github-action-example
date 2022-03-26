import unittest

from py_code import hello_world

class TestMethods(unittest.TestCase):
    def test_hello_world(self):
        hello_world.say_hi()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()